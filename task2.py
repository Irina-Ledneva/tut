time = int(input("Введите время в секундах : "))
hours = int(time / 3600)
time = time % 3600
minutes = int(time / 60)
seconds = time % 60
print(f"Время в формате ч:м:с - {hours} : {minutes} : {seconds} ")