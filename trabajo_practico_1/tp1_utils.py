
def set_table(df):
  '''Create a tabulated table using a given Data Frame'''
  table = []
  columns = df.columns
  for row in range(len(df.index)):
    table.append([])
    for elem in columns:
      table[row].append(df.at[row, elem])

  return table, columns

def test_chi_squared(data, n):
  ''''''
  deviations = []
  for index, row in data.iterrows():
    expected_frec = row['Probabilidad'] * n
    generated_frec = row['Simulación']
    deviations.append(pow(generated_frec - expected_frec, 2) / expected_frec)
  ji2 = 0
  for dev in deviations:
    ji2 += dev
  
  return ji2

def test_ks_distance(data):
  ks_distance = []
  for index, row in data.iterrows():
    ks_distance.append(abs(row['Sim Prob Acum'] - row['Probabilidad Acum']))
  
  return ks_distance