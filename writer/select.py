# Write SQL is a wrapper for generating SQL statements ia a set of standard rules

def select(table: str, fields: list = ["*", ], query_fields: list = None):
    '''Simple select returns a string SQL query by default it selects all unless specific fields are specified'''

    # Check all attributes are valid types including the attributes within the lists
    if isinstance(table, str) is False and isinstance(table, int) is False:
        raise TypeError(f"Table must be type list; currently {type(table)}")
    if isinstance(fields, list) is False:
        raise TypeError(f"Fields must be type list; currently {type(fields)}")
    if query_fields is not None and isinstance(query_fields, list) is False:
        raise TypeError(f"Match Fields must be type list; currently {type(query_fields)}")

    if fields is not None:
        count = 0
        for field in fields:
            if isinstance(field, str) is False and isinstance(field, int) is False:
                raise TypeError(f"Field[{count}] has invalid type: {type(field)}. Must be str or int")
            count += 1

    if query_fields is not None:
        count = 0
        for field in query_fields:
            if isinstance(field, str) is False and isinstance(field, int) is False:
                raise TypeError(f"Query Field[{count}] has invalid type: {type(field)}. Must be str or int")
            count += 1

    # Starts to create the sql statement here
    sql = "SELECT "
    if fields[0] == "*":
        sql = sql + "* "
    else:
        for field in fields:
            sql = sql + f"{field}, "
        sql = sql[:-2] + " "

    sql = sql + f"FROM {table}"

    if query_fields is not None:
        sql = sql + " WHERE "
        for field in query_fields:
            sql = sql + f"{field} = %s AND "
        sql = sql[:-5]

    return sql
