def menu():
    print("\n--- SMART TO-DO MANAGER ---")
    print("1. Tapşırıq əlavə et")
    print("2. Tapşırıqları göstər")
    print("3. Tapşırığı tamamlandı et")
    print("4. Tapşırığı sil")
    print("5. Çıxış")


def add_task():
    task = input("Yeni tapşırıq yaz: ")
    with open("tasks.txt", "a", encoding="utf-8") as file:
        file.write(task + " | ❌\n")
    print("Tapşırıq əlavə olundu.")


def show_tasks():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            tasks = file.readlines()
            if not tasks:
                print("Tapşırıq yoxdur.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("Tapşırıq tapılmadı.")


def complete_task():
    show_tasks()
    num = int(input("Tamamlanan tapşırığın nömrəsini seç: "))

    with open("tasks.txt", "r", encoding="utf-8") as file:
        tasks = file.readlines()

    tasks[num - 1] = tasks[num - 1].replace("❌", "✅")

    with open("tasks.txt", "w", encoding="utf-8") as file:
        file.writelines(tasks)

    print("Tapşırıq tamamlandı.")


def delete_task():
    show_tasks()
    num = int(input("Silinəcək tapşırığın nömrəsi: "))

    with open("tasks.txt", "r", encoding="utf-8") as file:
        tasks = file.readlines()

    tasks.pop(num - 1)

    with open("tasks.txt", "w", encoding="utf-8") as file:
        file.writelines(tasks)

    print("Tapşırıq silindi.")


while True:
    menu()
    choice = input("Seçim et (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Proqramdan çıxıldı.")
        break
    else:
        print("Yanlış seçim!")

