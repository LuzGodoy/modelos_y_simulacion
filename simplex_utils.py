"""Calculates cj and cj-zj and returns them as two dicts"""
def getcjzj(targetf, num_res, currentbase, df):
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
    if (maxi != max(maxi, cz[key])):
      maxi = cz[key]
      maxvar = key
  return maxvar


"""Gets minimun value within the cj-zj dict"""
def getminvar(cz):
  mini = 0
  minvar = None
  for key in cz.keys():
    if (mini != min(mini, cz[key])):
      mini = cz[key]
      minvar = key
  return minvar


""""""
def minimumexitbase(num_res, df, selected_column):
  mini = None
  minindex = None
  for i in range(num_res):
    if (mini == None):
      mini = df.at[i, selected_column]
  # TODO: Complete function


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