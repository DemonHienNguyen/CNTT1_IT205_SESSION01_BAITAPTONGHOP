import random
print("--- HỆ THỐNG THAM KHẢO BỆNH NHÂN ---")

name_patient = input("Vui lòng nhập tên bệnh nhân: ")

patient_gender = input("Vui lòng nhập giới tính của bạn: ")

patient_year_of_birth = int(input("Vui lòng nhập năm sinh của bạn: "))

patient_phoneNumber = input("Vui lòng nhập số điện thoại của bạn: ")

patient_email = input("Vui lòng nhập email của bệnh nhân: ")

patient_start_symptom = input("Vui lòng nhập triệu chứng ban đầu: ")

patient_total_cost = float(input("Vui lòng nhập chi phí khám: "))

patient_random_code = random.randint(100, 999)

patient_code = f"BN{patient_year_of_birth}{patient_random_code}"

print("--- THẺ BỆNH NHÂN ---")
print(f"Mã BN       : {patient_code}")
print(f"Tên         : {name_patient} ({type(name_patient).__name__})")
print(f"Giới tính   : {patient_gender} ({type(patient_gender).__name__})")
print(f"Năm sinh    : {patient_year_of_birth} ({type(patient_year_of_birth).__name__})")
print(f"Điện thoại  : {patient_phoneNumber} ({type(patient_phoneNumber).__name__})")
print(f"Email       : {patient_email} ({type(patient_email).__name__})")
print(f"Triệu chứng : {patient_start_symptom} ({type(patient_start_symptom).__name__})")
print(f"Chi phí     : {patient_total_cost} VND ({type(patient_total_cost).__name__})")
print("---------------------")