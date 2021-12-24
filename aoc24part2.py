from pyomo.environ import *

model = ConcreteModel()

model.w1 = Var(within=NonNegativeIntegers)
model.w2 = Var(within=NonNegativeIntegers)
model.w3 = Var(within=NonNegativeIntegers)
model.w4 = Var(within=NonNegativeIntegers)
model.w5 = Var(within=NonNegativeIntegers)
model.w6 = Var(within=NonNegativeIntegers)
model.w7 = Var(within=NonNegativeIntegers)
model.w8 = Var(within=NonNegativeIntegers)
model.w9 = Var(within=NonNegativeIntegers)
model.w10 = Var(within=NonNegativeIntegers)
model.w11 = Var(within=NonNegativeIntegers)
model.w12 = Var(within=NonNegativeIntegers)
model.w13 = Var(within=NonNegativeIntegers)
model.w14 = Var(within=NonNegativeIntegers)


def objectiveFunction(model):
    return(
        10**13*model.w1+10**12*model.w2+10**11*model.w3+10**10*model.w4
        + 10**9*model.w5+10**8*model.w6+10**7*model.w7+10**6*model.w8
        + 10**5*model.w9+10**4*model.w10+10**3*model.w11
        + 10**2*model.w12+10**1*model.w13+10**0*model.w14

    )


model.obj = Objective(rule=objectiveFunction, sense=minimize)

l = [
    model.w1, model.w2, model.w3, model.w4, model.w5, model.w6, model.w7, model.w8, model.w9,
    model.w10, model.w11, model.w12, model.w13, model.w14,
]

model.maxBounds = ConstraintList()
for w in l:
    lhs = w
    rhs = 9
    model.maxBounds.add(lhs <= rhs)

model.minBounds = ConstraintList()
for w in l:
    lhs = w
    rhs = 1
    model.minBounds.add(lhs >= rhs)

model.cs = ConstraintList()
model.cs.add(model.w4 == model.w3-2)
model.cs.add(model.w7 == model.w6-1)
model.cs.add(model.w9 == model.w8-3)
model.cs.add(model.w11 == model.w10-7)
model.cs.add(model.w12 == model.w5-5)
model.cs.add(model.w13 == model.w2+3)
model.cs.add(model.w14 == model.w1-4)

solver = SolverFactory('glpk')
results = solver.solve(model)

val = model.obj()
print('Solution: ', int(val))
