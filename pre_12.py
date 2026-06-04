

full_names = input("Enter full names : ").split(",")
initials = [f"{name.split()[0][0]}.{name.split()[1][0]}." 
            for name in full_names]
print(initials)     