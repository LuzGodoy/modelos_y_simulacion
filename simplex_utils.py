"""Calculates cj and cj-zj and returns them as two dicts"""
def getCjZj(targetf, num_res, currentbase, df):
  z = dict()
  cz = dict()
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


"""Checks whether the cjzj values meet the finish criteria or not"""
def finished(cz, args):
  if (args.maximize):
    if (cz[getmaxvar(cz)] <= 0):
      return True
    else:
      return False
  elif (args.minimize):
    if (cz[getminvar(cz)] >= 0):
      return True
    else:
      return False


"""Gets maximum value within the cj-zj dict"""
def getmaxvar(cz):
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


"""Gets minimun value within the cj-zj dict"""
def getminvar(cz):
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


"""Returns the index of the minimum value/solution to remove from the base"""
def minexitbase(num_res, df, selected_column):
  mini = None
  minindex = None
  for i in range(num_res):
    value = df.at[i, "Solution"] / df.at[i, selected_column]
    if (mini == None):
      mini = value
      minindex = i
    else:
      if (mini != min(mini, value)):
        mini = value
        minindex = i
  
  return minindex


"""Returns the index of the maximum value/solution to remove from the base"""
def maxexitbase(num_res, df, selected_column):
  maxi = None
  maxindex = None
  for i in range(num_res):
    value = df.at[i, "Solution"] / df.at[i, selected_column]
    if (maxi == None):
      maxi = value
      maxindex = i
    else:
      if (maxi != min(maxi, value)):
        maxi = value
        maxindex = i
  
  return maxindex


"""Returns new dataframe and base with updated values on the replaced row values"""
def replacebase(selected_column, base_index, base, df):
  new_df = df
  new_base = base
  new_base[base_index] = selected_column
  intersection = df.at[base_index, selected_column]
  for var in df.columns:
    new_df.at[base_index, var] = df.at[base_index, var] / intersection
  
  return new_df, new_base


"""Updates values on base rows according to the new replaced base values"""
def updatevalues(selected_column, replaced_index, base, df):
  new_df = df
  for index in base:
    if (index != replaced_index):
      multiplier = df.at[index, selected_column]
      for col in df.columns:
        new_df.at[index, col] = df.at[index, col] - (df.at[replaced_index, col] * multiplier)
  
  return new_df


"""Sets table structure for tabultation"""
def settable(num_res, df, targetf, base, zj, cjzj):
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