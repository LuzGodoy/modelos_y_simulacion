
def set_table(df):
    table = []
    columns = df.columns
    for row in range(len(df.index)):
        table.append([])
        for elem in columns:
            table[row].append(df.at[row, elem])
    return table, columns