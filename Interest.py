P=int(input("Enter The Princpal"))
R=int(input("Enter The rate Of Interest"))
T=int(input("Enter The Time"))
SI= (P*R*T)/100
CI= P*(1+(R/100))**T
print("The Simple Interest Is",SI)
print("The Compound Interest Is",CI)
