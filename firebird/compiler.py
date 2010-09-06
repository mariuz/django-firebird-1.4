from django.db.models.sql import compiler
from django.db.models.sql.query import get_order_dir
from django.db.models.sql.constants import *
from django.db.models.fields import AutoField

class SQLCompiler(compiler.SQLCompiler):
    def as_sql(self, with_limits=True, with_col_aliases=False):
        sql, params = super(SQLCompiler, self).as_sql(with_limits=False, with_col_aliases=with_col_aliases)
        
        if with_limits:
            limits = []
            if self.query.high_mark is not None:
                limits.append('FIRST %d' % (self.query.high_mark - self.query.low_mark))
            if self.query.low_mark:
                if self.query.high_mark is None:
                    val = self.connection.ops.no_limit_value()
                    if val:
                        limits.append('FIRST %d' % val)
                limits.append('SKIP %d' % self.query.low_mark)
            sql = 'SELECT %s %s' % (' '.join(limits), sql[6:].strip())
        return sql, params


class SQLInsertCompiler(compiler.SQLInsertCompiler, SQLCompiler):
    def _get_pk_next_value(self, db_table):
        seq_name = db_table.upper() + '_SEQ'
        if self.connection.ops.firebird_version[0] >= 2:
            return 'NEXT VALUE FOR %s' % seq_name
        else:
            cursor = self.connection.cursor()
            cursor.execute('SELECT GEN_ID(%s, 1) FROM rdb$database' % seq_name)
            id = cursor.fetchone()[0]
            return str(id)

    def _last_insert_id(self, cursor, model):
        seq_name = model._meta.db_table.upper() + '_SEQ'
        cursor.execute('SELECT GEN_ID(%s, 0) FROM rdb$database' % seq_name)
        return cursor.fetchone()[0]

    def as_sql(self):
        # We don't need quote_name_unless_alias() here, since these are all
        # going to be column names (so we can avoid the extra overhead).
        qn = self.connection.ops.quote_name
        opts = self.query.model._meta
        pk_auto = opts.pk and isinstance(opts.pk, AutoField)
        result = ['INSERT INTO %s' % qn(opts.db_table)]
        
        #result.append('(%s)' % ', '.join([qn(c) for c in self.query.columns]))
        cols = []
        if pk_auto:
            cols.append(qn(opts.pk.column))
        for c in self.query.columns:
            cols.append(qn(c))
        result.append('(%s)' % ', '.join([c for c in cols]))    
      
        #values = [self.placeholder(*v) for v in self.query.values]
        vals = []
        if pk_auto:
            vals.append(self._get_pk_next_value(opts.db_table))
        for v in self.query.values:
            vals.append(self.placeholder(*v))
        values = [v for v in vals]
        
        result.append('VALUES (%s)' % ', '.join(values))
        params = self.query.params
        if self.return_id and self.connection.features.can_return_id_from_insert:
            col = "%s.%s" % (qn(opts.db_table), qn(opts.pk.column))
            r_fmt, r_params = self.connection.ops.return_insert_id()
            result.append(r_fmt % col)
            params = params + r_params
        return ' '.join(result), params
    
    def execute_sql(self, return_id=False):
        self.return_id = return_id
        cursor = super(SQLInsertCompiler, self).execute_sql(None)
        if not (return_id and cursor):
            return
        if self.connection.features.can_return_id_from_insert:
            return self.connection.ops.fetch_returned_insert_id(cursor)
        return self._last_insert_id(cursor, self.query.model)


class SQLDeleteCompiler(compiler.SQLDeleteCompiler, SQLCompiler):
    pass

class SQLUpdateCompiler(compiler.SQLUpdateCompiler, SQLCompiler):
    pass

class SQLAggregateCompiler(compiler.SQLAggregateCompiler, SQLCompiler):
    pass

class SQLDateCompiler(compiler.SQLDateCompiler, SQLCompiler):
    pass

