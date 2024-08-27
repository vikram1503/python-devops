# There are 2 methods to create a tuple
# 1. ()
# 2. tuple()
# Behavior: They're immutable
sample_tuple = ("Ansible", "Terraform", "Jenkins", "Docker", "K8s") # Tool set

sample_ele = sample_tuple[0]
print(sample_ele)

sample_ele = sample_tuple[-1]
print(sample_ele)

# Slicing
sliced_tuple = sample_tuple[1:3] # ("Terraform", "Jenkins")
print(sliced_tuple)

sliced_tuple_len = len(sliced_tuple)
print(sliced_tuple_len)

""" sample_tuple[1] = "Shell"
print(sample_tuple) """

# Operations
res_tuple = sample_tuple + sliced_tuple
print(res_tuple) # ("Ansible", "Terraform", "Jenkins", "Docker", "K8s", "Terraform", "Jenkins")

res_tuple_1 = sliced_tuple * 2
print(res_tuple_1) # ("Terraform", "Jenkins", "Terraform", "Jenkins")

# Methods
k8s_idx = res_tuple.index("K8s")
print(k8s_idx)

# Tuple unpacking
ansible, terraform, jenkins, docker, k8s = ("Ansible", "Terraform", "Jenkins", "Docker", "K8s")

print(ansible, terraform, jenkins, docker, k8s)

ansible, *tools, orchestrator = ("Ansible", "Terraform", "Jenkins", "Docker", "K8s", "DevOps")

print(ansible, tools, orchestrator)
print(*tools)