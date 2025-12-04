import tkinter as tk
from tkinter import messagebox, ttk

# --- Thiết lập Hằng số Giao diện ---
LOGIN_BG = "#4d4d4d"
TEXT_COLOR = "#ffffff"
DASHBOARD_BG = "#f0f0f0"
WINDOW_TITLE_LOGIN = "Đăng nhập Hệ thống"
WINDOW_TITLE_MAIN = "Hệ thống Quản lý Điểm Sinh Viên"

class StudentScoreManagerApp:
    def __init__(self, master):
        self.master = master
        self.current_user = None

        # --- Dữ liệu Hệ thống ---
        self.user_database = {"admin": "123456"}
        self.chk_var = tk.IntVar()

        # Dữ liệu Sinh viên
        self.student_data = {
            "SV001": {"ten": "Nguyễn Văn Anh", "lop": "K18CNT", "khoa": "Công nghệ Thông tin"},
            "SV002": {"ten": "Trần Thị Bảo", "lop": "K19QTKD", "khoa": "Quản trị Kinh doanh"}
        }


        self.score_data = [
            {"ma_sv": "SV001", "mon_hoc": "Lập trình Python", "diem_tx1": 8.0, "diem_tx2": 9.0, "diem_cuoi_ky": 9.5,
             "hoc_ky": "HK1"},
            {"ma_sv": "SV001", "mon_hoc": "Toán rời rạc", "diem_tx1": 7.0, "diem_tx2": 6.5, "diem_cuoi_ky": 6.0,
             "hoc_ky": "HK1"},
            {"ma_sv": "SV002", "mon_hoc": "Kinh tế vi mô", "diem_tx1": 9.0, "diem_tx2": 9.5, "diem_cuoi_ky": 9.0,
             "hoc_ky": "HK1"}
        ]

        self.setup_login_ui()

    # --------------------------------------------------
    # --- PHẦN 1: LOGIC VÀ GIAO DIỆN ĐĂNG NHẬP (LOGIN) ---
    # --------------------------------------------------

    def setup_login_ui(self):
        self.master.title(WINDOW_TITLE_LOGIN)
        self.master.geometry("800x600")
        self.master.resizable(False, False)
        self.master.configure(bg=LOGIN_BG)

        tk.Label(self.master, text="QUẢN LÍ ĐIỂM SINH VIÊN",
                 font=("Segoe UI", 10, "bold"), bg=LOGIN_BG, fg=TEXT_COLOR,
                 anchor="w").pack(fill='x', padx=10, pady=(5, 50))

        main_content_frame = tk.Frame(self.master, bg=LOGIN_BG)
        main_content_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(main_content_frame, text="ĐĂNG NHẬP HỆ THỐNG",
                 font=("Segoe UI", 16, "bold"), bg=LOGIN_BG, fg=TEXT_COLOR).pack(pady=10)

        login_fields_frame = tk.Frame(main_content_frame, bg=LOGIN_BG)
        login_fields_frame.pack(pady=10)

        tk.Label(login_fields_frame, text="Tên tài khoản", bg=LOGIN_BG, fg=TEXT_COLOR).grid(row=0, column=0,
                                                                                             sticky="w", pady=5)
        self.entry_user = tk.Entry(login_fields_frame, width=25)
        self.entry_user.grid(row=0, column=1, padx=5, pady=5)
        self.entry_user.insert(0, "admin")

        tk.Label(login_fields_frame, text="Mật khẩu", bg=LOGIN_BG, fg=TEXT_COLOR).grid(row=1, column=0, sticky="w",
                                                                                        pady=5)
        self.entry_pass = tk.Entry(login_fields_frame, width=25, show="*")
        self.entry_pass.grid(row=1, column=1, padx=5, pady=5)
        self.entry_pass.insert(0, "123456")

        tk.Checkbutton(login_fields_frame, text="Xem mật khẩu", variable=self.chk_var,
                       command=self.toggle_password, bg=LOGIN_BG, fg=TEXT_COLOR, selectcolor=LOGIN_BG).grid(row=2,
                                                                                                              column=0,
                                                                                                              sticky="w",
                                                                                                              pady=10)

        forgot_pass_label = tk.Label(login_fields_frame, text="Quên mật khẩu?",
                                     bg=LOGIN_BG, fg=TEXT_COLOR,
                                     font=("Segoe UI", 9, "underline"), cursor="hand2")
        forgot_pass_label.grid(row=2, column=1, sticky="e", pady=10, padx=5)
        forgot_pass_label.bind("<Button-1>", self.forgot_password_action)

        button_container_frame = tk.Frame(main_content_frame, bg=LOGIN_BG)
        button_container_frame.pack(pady=15)

        tk.Button(button_container_frame, text="ĐĂNG NHẬP",
                  command=self.handle_login,
                  bg="#ffffff", fg="#000000",
                  font=("Segoe UI", 12, "bold"),
                  width=15, bd=0, relief=tk.FLAT).pack(side='left', padx=10)

        tk.Button(button_container_frame, text="ĐĂNG KÝ",
                  command=self.open_registration_form,
                  bg="#ffffff", fg="#000000",
                  font=("Segoe UI", 12, "bold"),
                  width=15, bd=0, relief=tk.FLAT).pack(side='left', padx=10)

    def toggle_password(self):
        self.entry_pass.config(show="" if self.chk_var.get() == 1 else "*")

    def handle_login(self):
        username = self.entry_user.get()
        password = self.entry_pass.get()

        if username in self.user_database and self.user_database[username] == password:
            messagebox.showinfo("Thông báo", "Đăng nhập thành công!")
            self.open_main_dashboard(username)
        else:
            messagebox.showerror("Lỗi", "Tên tài khoản hoặc Mật khẩu không đúng!")

    def open_registration_form(self):
        reg_window = tk.Toplevel(self.master)
        reg_window.title("Đăng ký Tài khoản")
        reg_window.geometry("500x400")
        reg_window.resizable(False, False)
        reg_window.configure(bg=LOGIN_BG)

        tk.Label(reg_window, text="ĐĂNG KÝ TÀI KHOẢN MỚI",
                 font=("Segoe UI", 14, "bold"), bg=LOGIN_BG, fg=TEXT_COLOR).pack(pady=10)

        reg_frame = tk.Frame(reg_window, bg=LOGIN_BG, padx=20, pady=10)
        reg_frame.pack(pady=10)

        tk.Label(reg_frame, text="Tên tài khoản:", font=("Segoe UI", 10), bg=LOGIN_BG, fg=TEXT_COLOR).grid(row=0,
                                                                                                            column=0,
                                                                                                            sticky="w",
                                                                                                            pady=5)
        reg_user_entry = tk.Entry(reg_frame, width=30)
        reg_user_entry.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(reg_frame, text="Mật khẩu:", font=("Segoe UI", 10), bg=LOGIN_BG, fg=TEXT_COLOR).grid(row=1, column=0,
                                                                                                       sticky="w",
                                                                                                       pady=5)
        reg_pass_entry = tk.Entry(reg_frame, show="*", width=30)
        reg_pass_entry.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(reg_frame, text="Xác nhận MK:", font=("Segoe UI", 10), bg=LOGIN_BG, fg=TEXT_COLOR).grid(row=2,
                                                                                                          column=0,
                                                                                                          sticky="w",
                                                                                                          pady=5)
        reg_confirm_entry = tk.Entry(reg_frame, show="*", width=30)
        reg_confirm_entry.grid(row=2, column=1, pady=5, padx=5)

        def register_user():
            username = reg_user_entry.get()
            password = reg_pass_entry.get()
            confirm_pass = reg_confirm_entry.get()

            if not all([username, password, confirm_pass]):
                messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!", parent=reg_window)
                return

            if password != confirm_pass:
                messagebox.showerror("Lỗi", "Mật khẩu không khớp!", parent=reg_window)
            elif username in self.user_database:
                messagebox.showerror("Lỗi", "Tên tài khoản đã tồn tại!", parent=reg_window)
            else:
                self.user_database[username] = password
                messagebox.showinfo("Thành công", f"Đăng ký '{username}' thành công!", parent=reg_window)
                reg_window.destroy()

        tk.Button(reg_window, text="ĐĂNG KÝ", command=register_user,
                  bg="#ffffff", fg="#000000", font=("Segoe UI", 11, "bold")).pack(pady=10)

    def open_forgot_password_form(self):
        forgot_window = tk.Toplevel(self.master)
        forgot_window.title("Khôi phục Mật khẩu")
        forgot_window.geometry("400x200")
        forgot_window.resizable(False, False)
        forgot_window.configure(bg=LOGIN_BG)

        tk.Label(forgot_window, text="KHÔI PHỤC MẬT KHẨU",
                 font=("Segoe UI", 14, "bold"), bg=LOGIN_BG, fg=TEXT_COLOR).pack(pady=10)

        forgot_frame = tk.Frame(forgot_window, bg=LOGIN_BG)
        forgot_frame.pack(pady=10)

        tk.Label(forgot_frame, text="Tên tài khoản:", font=("Segoe UI", 10), bg=LOGIN_BG, fg=TEXT_COLOR).grid(row=0,
                                                                                                               column=0,
                                                                                                               sticky="w",
                                                                                                               pady=5)
        user_entry = tk.Entry(forgot_frame, width=25)
        user_entry.grid(row=0, column=1, pady=5, padx=5)

        def recover_password():
            username = user_entry.get()
            if not username:
                messagebox.showwarning("Cảnh báo", "Vui lòng nhập Tên tài khoản.", parent=forgot_window)
                return

            if username in self.user_database:
                messagebox.showinfo("Thành công",
                                    f"Yêu cầu khôi phục cho tài khoản '{username}' đã được ghi nhận. \n"
                                    f"Vui lòng kiểm tra email của bạn để đặt lại mật khẩu.",
                                    parent=forgot_window)
                forgot_window.destroy()
            else:
                messagebox.showerror("Lỗi", "Tên tài khoản không tồn tại.", parent=forgot_window)

        tk.Button(forgot_frame, text="KHÔI PHỤC", command=recover_password,
                  bg="#ffffff", fg="#000000", font=("Segoe UI", 11, "bold")).grid(row=1, column=0, columnspan=2,
                                                                                  pady=15)

    def forgot_password_action(self, event):
        self.open_forgot_password_form()

    # --------------------------------------------------------
    # --- PHẦN 2: CHUYỂN ĐỔI VÀ GIAO DIỆN CHÍNH (DASHBOARD) ---
    # --------------------------------------------------------

    def open_main_dashboard(self, user_id):
        self.current_user = user_id

        for widget in self.master.winfo_children():
            widget.destroy()

        self.master.title(f"{WINDOW_TITLE_MAIN} - Chào mừng {user_id}")
        self.master.geometry("1100x700")
        self.master.resizable(True, True)
        self.master.configure(bg=DASHBOARD_BG)

        self.setup_dashboard_ui()

    def setup_style(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Segoe UI", 10), background=DASHBOARD_BG)
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
        style.configure("TNotebook.Tab", font=("Segoe UI", 11, "bold"))
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
        style.map("TButton", background=[("active", "#d4d4d4")])
        style.configure("TFrame", background=DASHBOARD_BG)

    def setup_dashboard_ui(self):
        self.setup_style()

        notebook_frame = ttk.Frame(self.master, padding="10")
        notebook_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.notebook = ttk.Notebook(notebook_frame)
        self.notebook.pack(fill="both", expand=True)

        self.create_tab_quan_ly_sinh_vien(self.notebook)
        self.create_tab_quan_ly_diem(self.notebook)

        tk.Button(self.master, text="ĐĂNG XUẤT", command=self.master.quit,
                  bg="#cc0000", fg="white", font=("Segoe UI", 11, "bold"),
                  width=15, relief=tk.FLAT).pack(pady=10)

    # ----------------------------------------------------
    # --- PHẦN 3: LOGIC QUẢN LÝ SINH VIÊN (SV MANAGER) ---
    # ----------------------------------------------------

    def refresh_sv_tree(self):
        for item in self.sv_tree.get_children():
            self.sv_tree.delete(item)

        for ma_sv, data in self.student_data.items():
            self.sv_tree.insert("", tk.END, values=(ma_sv, data['ten'], data['lop'], data['khoa']), iid=ma_sv)

    def load_student_to_form(self, event):
        selected_item = self.sv_tree.focus()
        if selected_item:
            ma_sv = selected_item
            data = self.student_data.get(ma_sv)
            if data:
                self.sv_ma_entry.config(state='normal')
                self.sv_ma_entry.delete(0, tk.END)
                self.sv_ma_entry.insert(0, ma_sv)
                self.sv_ma_entry.config(state='disabled')

                self.sv_ten_entry.delete(0, tk.END)
                self.sv_ten_entry.insert(0, data['ten'])

                self.sv_lop_entry.delete(0, tk.END)
                self.sv_lop_entry.insert(0, data['lop'])

                self.sv_khoa_entry.delete(0, tk.END)
                self.sv_khoa_entry.insert(0, data['khoa'])
        else:
            self.clear_sv_form()

    def clear_sv_form(self):
        self.sv_ma_entry.config(state='normal')
        self.sv_ma_entry.delete(0, tk.END)
        self.sv_ten_entry.delete(0, tk.END)
        self.sv_lop_entry.delete(0, tk.END)
        self.sv_khoa_entry.delete(0, tk.END)

    def get_sv_form_data(self):
        ma_sv = self.sv_ma_entry.get().strip()
        ten_sv = self.sv_ten_entry.get().strip()
        lop = self.sv_lop_entry.get().strip()
        khoa = self.sv_khoa_entry.get().strip()
        return ma_sv, ten_sv, lop, khoa

    def add_student(self):
        ma_sv, ten_sv, lop, khoa = self.get_sv_form_data()

        if not all([ma_sv, ten_sv, lop, khoa]):
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin Sinh Viên.")
            return

        if ma_sv in self.student_data:
            messagebox.showerror("Lỗi", f"Mã Sinh Viên '{ma_sv}' đã tồn tại. Vui lòng chọn Sửa nếu muốn cập nhật.")
            return

        self.student_data[ma_sv] = {"ten": ten_sv, "lop": lop, "khoa": khoa}
        messagebox.showinfo("Thành công", f"Đã thêm Sinh Viên: {ten_sv}")
        self.refresh_sv_tree()
        self.clear_sv_form()

    def edit_student(self):
        ma_sv, ten_sv, lop, khoa = self.get_sv_form_data()

        if not ma_sv or ma_sv not in self.student_data:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn Sinh Viên cần sửa trong bảng.")
            return

        if not all([ten_sv, lop, khoa]):
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin Sinh Viên.")
            return

        self.student_data[ma_sv] = {"ten": ten_sv, "lop": lop, "khoa": khoa}
        messagebox.showinfo("Thành công", f"Đã cập nhật thông tin cho: {ten_sv}")
        self.refresh_sv_tree()
        self.clear_sv_form()

    def delete_student(self):
        ma_sv = self.sv_ma_entry.get().strip()

        if not ma_sv or ma_sv not in self.student_data:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn Sinh Viên cần xóa trong bảng.")
            return

        if messagebox.askyesno("Xác nhận Xóa",
                               f"Bạn có chắc chắn muốn xóa Sinh Viên '{self.student_data[ma_sv]['ten']}' (Mã: {ma_sv})?"
                               f"\nLưu ý: Điểm của Sinh Viên này cũng sẽ bị xóa."):
            del self.student_data[ma_sv]

            self.score_data = [score for score in self.score_data if score['ma_sv'] != ma_sv]

            messagebox.showinfo("Thành công", "Đã xóa Sinh Viên thành công.")
            self.refresh_sv_tree()
            self.clear_sv_form()
            self.refresh_diem_tree()

    def create_tab_quan_ly_sinh_vien(self, notebook):
        tab = ttk.Frame(notebook, padding="10")
        notebook.add(tab, text='Quản lý Sinh Viên')

        main_frame = ttk.Frame(tab, padding="15", relief="groove")
        main_frame.pack(side="top", fill="both", expand=True)

        ttk.Label(main_frame, text="DANH SÁCH SINH VIÊN", font=("Segoe UI", 14, "bold")).pack(pady=(0, 15), anchor="w")

        entry_frame = ttk.Frame(main_frame)
        entry_frame.pack(fill="x", pady=10)

        ttk.Label(entry_frame, text="Mã Sinh Viên:").pack(side="left", padx=5)
        self.sv_ma_entry = ttk.Entry(entry_frame, width=12)
        self.sv_ma_entry.pack(side="left", padx=5)

        ttk.Label(entry_frame, text="Tên Sinh Viên:").pack(side="left", padx=5)
        self.sv_ten_entry = ttk.Entry(entry_frame, width=30)
        self.sv_ten_entry.pack(side="left", padx=5)

        ttk.Label(entry_frame, text="Lớp:").pack(side="left", padx=5)
        self.sv_lop_entry = ttk.Entry(entry_frame, width=10)
        self.sv_lop_entry.pack(side="left", padx=5)

        ttk.Label(entry_frame, text="Khoa:").pack(side="left", padx=5)
        self.sv_khoa_entry = ttk.Entry(entry_frame, width=20)
        self.sv_khoa_entry.pack(side="left", padx=5)

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Thêm Sinh Viên", command=self.add_student).pack(side="left", padx=10)
        ttk.Button(button_frame, text="Sửa Thông Tin", command=self.edit_student).pack(side="left", padx=10)
        ttk.Button(button_frame, text="Xóa Sinh Viên", command=self.delete_student).pack(side="left", padx=10)

        columns = ("Mã Sinh Viên", "Tên Sinh Viên", "Lớp", "Khoa")
        self.sv_tree = ttk.Treeview(main_frame, columns=columns, show="headings", height=15)

        self.sv_tree.heading("Mã Sinh Viên", text="Mã Sinh Viên")
        self.sv_tree.heading("Tên Sinh Viên", text="Tên Sinh Viên")
        self.sv_tree.heading("Lớp", text="Lớp")
        self.sv_tree.heading("Khoa", text="Khoa")

        self.sv_tree.column("Mã Sinh Viên", width=100, anchor=tk.CENTER)
        self.sv_tree.column("Tên Sinh Viên", width=200)
        self.sv_tree.column("Lớp", width=100, anchor=tk.CENTER)
        self.sv_tree.column("Khoa", width=150)

        self.sv_tree.pack(fill="both", expand=True, pady=10)
        self.sv_tree.bind('<<TreeviewSelect>>', self.load_student_to_form)
        self.refresh_sv_tree()

    # ------------------------------------------------
    # --- PHẦN 4: LOGIC QUẢN LÝ ĐIỂM (SCORE MANAGER) ---
    # ------------------------------------------------

    def calculate_entry_avg(self, score_entry):
        try:
            tx1 = score_entry['diem_tx1']
            tx2 = score_entry['diem_tx2']
            ck = score_entry['diem_cuoi_ky']

            diem_tb = (tx1 + tx2 + ck) / 3

            return round(diem_tb, 2)
        except (TypeError, KeyError):
            return 0

    def get_diem_form_data(self):
        ma_sv = self.diem_ma_sv_entry.get().strip()
        mon_hoc = self.diem_mon_hoc_cbox.get().strip()
        hoc_ky = self.diem_hk_cbox.get().strip()

        diem_strings = {
            "diem_tx1": self.diem_tx1_entry.get().strip(),
            "diem_tx2": self.diem_tx2_entry.get().strip(),
            "diem_cuoi_ky": self.diem_ck_entry.get().strip(),
        }

        if not all([ma_sv, mon_hoc != "Chọn Môn học", hoc_ky != "Chọn Học kỳ"] + list(diem_strings.values())):
            messagebox.showwarning("Cảnh báo",
                                   "Vui lòng nhập đầy đủ thông tin Điểm (Mã SV, Môn, 3 cột Điểm: Tx1, Tx2, CK, Học kỳ).")
            return None, None, None, None

        scores_dict = {}
        for key, diem_str in diem_strings.items():
            try:
                diem = float(diem_str)
                if not (0 <= diem <= 10):
                    messagebox.showerror("Lỗi", "Tất cả điểm phải là giá trị từ 0 đến 10.")
                    return None, None, None, None
                scores_dict[key] = diem
            except ValueError:
                messagebox.showerror("Lỗi", "Điểm nhập vào không hợp lệ (phải là số).")
                return None, None, None, None

        return ma_sv, mon_hoc, hoc_ky, scores_dict

    def refresh_diem_tree(self):
        for item in self.diem_tree.get_children():
            self.diem_tree.delete(item)

        for index, score in enumerate(self.score_data):
            ten_sv = self.student_data.get(score['ma_sv'], {}).get('ten', 'Không rõ')

            diem_tb = self.calculate_entry_avg(score)

            values = (
                score['ma_sv'], ten_sv, score['mon_hoc'],
                score['diem_tx1'], score['diem_tx2'],
                score['diem_cuoi_ky'],
                score['hoc_ky'],
                diem_tb
            )
            self.diem_tree.insert("", tk.END, values=values, iid=str(index))

    def load_score_to_form(self, event):
        selected_iid = self.diem_tree.focus()
        if selected_iid:
            try:
                index = int(selected_iid)
                score = self.score_data[index]

                self.diem_ma_sv_entry.delete(0, tk.END)
                self.diem_ma_sv_entry.insert(0, score['ma_sv'])

                self.diem_mon_hoc_cbox.set(score['mon_hoc'])

                self.diem_tx1_entry.delete(0, tk.END)
                self.diem_tx1_entry.insert(0, str(score['diem_tx1']))
                self.diem_tx2_entry.delete(0, tk.END)
                self.diem_tx2_entry.insert(0, str(score['diem_tx2']))

                self.diem_ck_entry.delete(0, tk.END)
                self.diem_ck_entry.insert(0, str(score['diem_cuoi_ky']))

                self.diem_hk_cbox.set(score['hoc_ky'])
            except IndexError:
                pass

    def clear_diem_form(self):
        self.diem_ma_sv_entry.delete(0, tk.END)
        self.diem_mon_hoc_cbox.set("Chọn Môn học")

        self.diem_tx1_entry.delete(0, tk.END)
        self.diem_tx2_entry.delete(0, tk.END)
        self.diem_ck_entry.delete(0, tk.END)

        self.diem_hk_cbox.set("Chọn Học kỳ")

    def add_score(self):
        ma_sv, mon_hoc, hoc_ky, scores_dict = self.get_diem_form_data()

        if not scores_dict: return

        if ma_sv not in self.student_data:
            messagebox.showerror("Lỗi", f"Mã Sinh Viên '{ma_sv}' không tồn tại trong hệ thống.")
            return

        new_score = {"ma_sv": ma_sv, "mon_hoc": mon_hoc, "hoc_ky": hoc_ky}
        new_score.update(scores_dict)

        self.score_data.append(new_score)

        messagebox.showinfo("Thành công", f"Đã thêm điểm cho Sinh Viên {ma_sv}, môn {mon_hoc}.")
        self.refresh_diem_tree()
        self.clear_diem_form()

    def edit_score(self):
        selected_iid = self.diem_tree.focus()
        if not selected_iid:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một hàng điểm để sửa.")
            return

        index = int(selected_iid)

        ma_sv, mon_hoc, hoc_ky, scores_dict = self.get_diem_form_data()

        if not scores_dict: return

        updated_score = {"ma_sv": ma_sv, "mon_hoc": mon_hoc, "hoc_ky": hoc_ky}
        updated_score.update(scores_dict)

        self.score_data[index] = updated_score

        messagebox.showinfo("Thành công", "Đã cập nhật điểm thành công.")
        self.refresh_diem_tree()
        self.clear_diem_form()

    def delete_score(self):
        selected_iid = self.diem_tree.focus()
        if not selected_iid:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một hàng điểm để xóa.")
            return

        index = int(selected_iid)

        if messagebox.askyesno("Xác nhận Xóa", "Bạn có chắc chắn muốn xóa mục điểm này?"):
            self.score_data.pop(index)
            messagebox.showinfo("Thành công", "Đã xóa điểm thành công.")
            self.refresh_diem_tree()
            self.clear_diem_form()

    def create_tab_quan_ly_diem(self, notebook):
        tab = ttk.Frame(notebook, padding="15")
        notebook.add(tab, text='Quản lý Điểm')

        ttk.Label(tab, text="NHẬP VÀ XEM ĐIỂM SINH VIÊN", font=("Segoe UI", 14, "bold")).pack(pady=(0, 15), anchor="w")

        input_frame = ttk.Frame(tab, padding="10", relief="sunken")
        input_frame.pack(fill="x", pady=10)

        ttk.Label(input_frame, text="Mã SV:").pack(side="left", padx=5)
        self.diem_ma_sv_entry = ttk.Entry(input_frame, width=10)
        self.diem_ma_sv_entry.pack(side="left", padx=5)

        ttk.Label(input_frame, text="Môn:").pack(side="left", padx=5)
        self.diem_mon_hoc_cbox = ttk.Combobox(input_frame, width=15,
                                              values=["Cấu trúc Dữ liệu", "Lập trình Python", "Toán rời rạc",
                                                      "Kinh tế vi mô", "Toán A3"])
        self.diem_mon_hoc_cbox.pack(side="left", padx=5)
        self.diem_mon_hoc_cbox.set("Chọn Môn học")

        ttk.Label(input_frame, text="Tx1:").pack(side="left", padx=(15, 2))
        self.diem_tx1_entry = ttk.Entry(input_frame, width=5)
        self.diem_tx1_entry.pack(side="left", padx=2)

        ttk.Label(input_frame, text="Tx2:").pack(side="left", padx=2)
        self.diem_tx2_entry = ttk.Entry(input_frame, width=5)
        self.diem_tx2_entry.pack(side="left", padx=2)

        ttk.Label(input_frame, text="CK:").pack(side="left", padx=2)
        self.diem_ck_entry = ttk.Entry(input_frame, width=5)
        self.diem_ck_entry.pack(side="left", padx=5)

        ttk.Label(input_frame, text="Học kỳ:").pack(side="left", padx=(15, 5))
        self.diem_hk_cbox = ttk.Combobox(input_frame, width=10,
                                         values=["HK1", "HK2", "Hè"])
        self.diem_hk_cbox.pack(side="left", padx=5)
        self.diem_hk_cbox.set("Chọn Học kỳ")

        button_frame = ttk.Frame(tab)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Thêm Điểm", command=self.add_score).pack(side="left", padx=10)
        ttk.Button(button_frame, text="Sửa Điểm", command=self.edit_score).pack(side="left", padx=10)
        ttk.Button(button_frame, text="Xóa Điểm", command=self.delete_score).pack(side="left", padx=10)

        ttk.Label(tab, text="BẢNG ĐIỂM CHI TIẾT ",
                  font=("Segoe UI", 12, "bold")).pack(pady=(15, 10), anchor="w")

        columns = ("Mã Sinh Viên", "Tên Sinh Viên", "Môn học", "Tx1", "Tx2", "CK", "Học kỳ", "Điểm TB")
        self.diem_tree = ttk.Treeview(tab, columns=columns, show="headings", height=15)

        self.diem_tree.heading("Mã Sinh Viên", text="Mã SV")
        self.diem_tree.heading("Tên Sinh Viên", text="Tên Sinh Viên")
        self.diem_tree.heading("Môn học", text="Môn học")
        self.diem_tree.heading("Tx1", text="Tx1")
        self.diem_tree.heading("Tx2", text="Tx2")
        self.diem_tree.heading("CK", text="CK")
        self.diem_tree.heading("Học kỳ", text="HK")
        self.diem_tree.heading("Điểm TB", text="ĐTB")

        self.diem_tree.column("Mã Sinh Viên", width=80, anchor=tk.CENTER)
        self.diem_tree.column("Tên Sinh Viên", width=150)
        self.diem_tree.column("Môn học", width=150)
        self.diem_tree.column("Tx1", width=50, anchor=tk.CENTER)
        self.diem_tree.column("Tx2", width=50, anchor=tk.CENTER)
        self.diem_tree.column("CK", width=50, anchor=tk.CENTER)
        self.diem_tree.column("Học kỳ", width=50, anchor=tk.CENTER)
        self.diem_tree.column("Điểm TB", width=70, anchor=tk.CENTER)

        self.diem_tree.pack(fill="both", expand=True, pady=5)
        self.diem_tree.bind('<<TreeviewSelect>>', self.load_score_to_form)
        self.refresh_diem_tree()


if __name__ == '__main__':
    root = tk.Tk()
    app = StudentScoreManagerApp(root)
    root.mainloop()