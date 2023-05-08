
def get_cjzj(targetf, num_res, currentbase, df):
  """Calculates cj and cj-zj and returns them as two dicts"""
  z = dict(); cz = dict()
  for var in targetf.keys():
    acum = 0
    for i in range(num_res):
      acum += targetf[currentbase[i]] * df.at[i, var]
    z[var] = acum
    cz[var] = targetf[var] - z[var]
  acum_solution = 0
  for i in range(num_res):
    acum_solution += df.at[i, "Solution"] * targetf[currentbase[i]]
  z["Solution"] = acum_solution
  
  return z, cz


def is_finished(cz, args):
  """Checks whether the cjzj values meet the finish criteria or not"""
  if (args.maximize):
    return cz[get_max_var(cz)] <= 0
  elif (args.minimize):
    return cz[get_min_var(cz)] >= 0


def get_max_var(cz):
  """Gets maximum value within the cj-zj dict"""
  maxi = 0
  maxvar = None
  for key in cz.keys():
    if (maxvar == None):
      maxi = cz[key]
      maxvar = key
    else:
      if (maxi != max(maxi, cz[key])):
        maxi = cz[key]
        maxvar = key
  
  return maxvar


def get_min_var(cz):
  """Gets minimun value within the cj-zj dict"""
  mini = 0
  minvar = None
  for key in cz.keys():
    if (minvar == None):
      mini = cz[key]
      minvar = key
    else:
      if (mini != min(mini, cz[key])):
        mini = cz[key]
        minvar = key
  
  return minvar


def min_exit_base(num_res, df, selected_column):
  """Returns the index of the minimum value/solution to remove from the base, returns None if there are no valid options"""
  mini = None
  min_index = None
  for i in range(num_res):
    if (df.at[i, selected_column] > 0):
      value = df.at[i, "Solution"] / df.at[i, selected_column]
      if (mini == None):
        mini = value
        min_index = i
      else:
        if (mini != min(mini, value)):
          mini = value
          min_index = i
  
  return min_index


def replace_base(selected_column, base_index, base, df):
  """Returns new dataframe and base with updated values on the replaced row values"""
  new_df = df
  new_base = base
  new_base[base_index] = selected_column
  intersection = df.at[base_index, selected_column]
  for var in df.columns:
    new_df.at[base_index, var] = df.at[base_index, var] / intersection
  
  return new_df, new_base


def update_values(selected_column, replaced_index, base, df):
  """Updates values on base rows according to the new replaced base values"""
  new_df = df
  for index in base:
    if (index != replaced_index):
      multiplier = df.at[index, selected_column]
      for col in df.columns:
        new_df.at[index, col] = df.at[index, col] - (df.at[replaced_index, col] * multiplier)
  
  return new_df


def set_table(num_res, df, targetf, base, zj, cjzj):
  """Sets table structure for tabultation"""
  columns = ["", ""]
  table = []
  for var in targetf.keys():
    columns.append(var)
  columns.append("")
  table.append([])
  table[0].append("Base")
  table[0].append("Cj")
  for var in targetf.keys():
    table[0].append(targetf[var])
  table[0].append("Solucion")
  for i in range(num_res):
    table.append([])
    table[i+1].append(base[i])
    table[i+1].append(targetf[base[i]])
    for var in targetf.keys():
      table[i+1].append(df.at[i, var])
    table[i+1].append(df.at[i, "Solution"])
  table.append([])
  lastindex = len(table)-1
  table[lastindex].append("")
  table[lastindex].append("Zj")
  for key in zj.keys():
    table[lastindex].append(zj[key])
  table.append([])
  lastindex = len(table)-1
  table[lastindex].append("")
  table[lastindex].append("Cj-Zj")
  for key in cjzj.keys():
    table[lastindex].append(cjzj[key])
  table[lastindex].append("")
  
  return table, columns