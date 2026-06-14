def show_menu():
    print("\n" + "="*50)
    print("      SMART ENERGY MONITOR - PHÒNG CƠ ĐIỆN      ")
    print("="*50)
    print("1. Xem danh sách thiết bị giám sát")
    print("2. Cập nhật chỉ số điện tiêu thụ (Check-in)")
    print("3. Kích hoạt trạng thái cảnh báo quá tải")
    print("4. Tính tổng lượng điện & Chi phí năng lượng")
    print("5. Thoát chương trình")
    print("="*50)

def main():
    devices = [
        {'id': 'M01', 'location': 'Mechanical Shop A', 'old_index': 1200, 'new_index': 4500, 'status': 'Normal'},
        {'id': 'M02', 'location': 'Assembly Line B', 'old_index': 2300, 'new_index': 8500, 'status': 'Overload'}
    ]
    
    while True:
        show_menu()
        
        try:
            choice = int(input("Mời chọn chức năng (1-5): "))
        except ValueError:
            print("[LỖI] Vui lòng chỉ nhập số nguyên từ 1 đến 5!")
            continue
            
        if choice == 1:
            print("\n--> Bạn đã chọn Chức năng 1: Xem danh sách thiết bị.")
            
        elif choice == 2:
            print("\n--> Bạn đã chọn Chức năng 2: Cập nhật chỉ số điện tiêu thụ.")
            
        elif choice == 3:
            print("\n--> Bạn đã chọn Chức năng 3: Kích hoạt trạng thái cảnh báo quá tải.")
            
        elif choice == 4:
            print("\n--> Bạn đã chọn Chức năng 4: Tính tổng lượng điện & Chi phí năng lượng.")
            
        elif choice == 5:
            print("\nCảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")
            break
            
        else:
            print("[LỖI] Lựa chọn không hợp lệ! Vui lòng chọn lại từ 1 đến 5.")

main()