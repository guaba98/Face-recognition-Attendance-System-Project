import psycopg2

host = "10.10.20.103"
port = "5432"
database = "ATD"
name = "postgres"
password = "1234"

class DBconnect:
    def __init__(self, controller):
        self.controller = controller
        self.conn = None
        self.cur = None
        # self.start_conn()
    def start_conn(self):
        self.conn = psycopg2.connect(host=host, database=database, user=name, password=password, port=port)
        self.cur = self.conn.cursor()

        return self.cur

    def commit_db(self):
        if self.conn is not None:
            self.conn.commit()

    def end_conn(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    # 출근 데이터 저장
    def log_in(self, user_id, day_date, time_date):
        user_no = self.find_no(user_id)
        clock_in = self.clock_in_check(user_no) # 출근 여부 출근 안했으면 0, 했으면 1
        c = self.start_conn()
        if user_no != None:
            if clock_in == 0:
                clock_in_query = "insert into tb_atd (user_no, atd_date, atd_time, atd_start, atd_end, atd_type) " \
                                 f"values('{user_no}', '{day_date}','{time_date}',1,0,'face')"
                c.execute(clock_in_query)
                self.commit_db()
                self.end_conn()
                return True
        else:
            self.end_conn()
            return False # 등록된 사원이 아니면 False를 리턴함


    # user_no 찾는 함수
    def find_no(self, user_id):
        c = self.start_conn()
        no_query = f"select user_no from tb_user where user_id = '{user_id}'"  # user_no 찾는 쿼리
        c.execute(no_query)  # user_no 찾는 쿼리문 실행
        data = c.fetchone()  # user_no
        if data != None:
            self.end_conn()
            return data[0]
        else:
            self.end_conn()
            return None


    # 출근 여부 확인
    def clock_in_check(self, user_no):
        c = self.start_conn()
        check_query = f"select atd_start from tb_atd where user_no = '{user_no}'"
        c.execute(check_query)
        data = c.fetchone()
        if data != None:
            return data[0]
        else:
            return 0
        self.end_conn()

    def regiseter_info(self):
        c = self.start_conn()

    # 부서 목록 이름만 담아서 리스트로 반환
    def find_dept(self):
        dept_list = list()
        c = self.start_conn()
        dept_query = "select dept_name from tb_dept group by dept_name"
        c.execute(dept_query)
        datas = c.fetchall()
        for data in datas:
            name = data[0]
            dept_list.append(name)

        return dept_list

    # 선택한 부서별 사원만 리스트 담아서 리턴
    def select_dept(self, dept):
        empolyee_list = list()
        c = self.start_conn()
        empolyee_query = "select tb_user.user_name from tb_user join tb_dept on tb_user.dept_id = tb_dept.dept_id " \
                         f"where tb_dept.dept_name = '{dept}'"
        c.execute(empolyee_query)
        datas = c.fetchall()
        for data in datas:
            empolyee_name = data[0]
            empolyee_list.append(empolyee_name)

        return empolyee_list



if __name__ == '__main__':
    db_conn = DBconnect(controller=None)
    a = db_conn.select_dept('인사팀')



