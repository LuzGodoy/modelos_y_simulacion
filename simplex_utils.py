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

