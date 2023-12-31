import psycopg2
from datetime import datetime, date

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
    def log_in(self, user_id, day_date, time_date, login_type):
        user_no = self.find_no(user_id)
        clock_in = self.clock_in_check(user_no, day_date)  # 출근 여부 출근 안했으면 0, 했으면 1
        c = self.start_conn()
        if user_no != None:
            if clock_in == 0:
                clock_in_query = "insert into tb_atd (user_no, atd_date, atd_time, atd_start, atd_end, atd_type, atd_leave) " \
                                 f"values('{user_no}', '{day_date}','{time_date}',1,0,'{login_type}', 'NULL')"
                c.execute(clock_in_query)
                self.commit_db()
                self.end_conn()
                return True
        else:
            self.end_conn()
            return False  # 등록된 사원이 아니면 False를 리턴함

    # user_no 찾는 함수
    def find_no(self, user_id):
        c = self.start_conn()
        no_query = f"select user_no from tb_user where user_id = '{user_id}'"
        # no_query = f"select tb_user.user_no from tb_user join tb_atd on tb_user.user_no = tb_atd.user_no " \
        #            f"where tb_user.user_id = '{user_id}' and tb_atd.atd_date = '{day_date}'"  # user_no 찾는 쿼리
        c.execute(no_query)  # user_no 찾는 쿼리문 실행
        data = c.fetchone()  # user_no
        if data != None:
            self.end_conn()
            return data[0]
        else:
            self.end_conn()
            return None

    from datetime import datetime

    def return_datetime(self, type):
        """원하는 날짜/시간 포멧을 반환"""
        now = datetime.now()  # 시간

        if type == 'date':
            now_format = now.strftime("%Y-%m-%d")  # 년 월 일
        elif type == 'time':
            now_format = now.strftime("%Y-%m-%d %H:%M:%S")  # 년 월 일 시 분 초
        elif type == 'time_only':
            now_format = now.strftime("%H:%M:%S")  # 시 분 초
        elif type == 'year_month':
            now_format = now.strftime("%Y-%m")  # 년월
        elif type == 'c_date':
            now_format = now.strftime("%d")  # 일
        else:
            return "Invalid type"

        # print('[dateimte.py]시간 포멧팅: ', now_format)
        return now_format

    def get_strptime(self, start_time_str, end_time_str):
        start_time_obj = datetime.strptime(start_time_str, '%H:%M:%S')
        end_time_obj = datetime.strptime(end_time_str, '%H:%M:%S')

        # 두 시간 간의 차이 계산
        time_difference = end_time_obj - start_time_obj
        return time_difference

    # 요일로 반환
    def get_day_of_week(self, text_date):

        date_object = datetime.strptime(text_date, '%Y-%m-%d').date()
        # 요일을 숫자로 반환 (월요일: 0, 화요일: 1, ..., 일요일: 6)
        day_of_week = date_object.weekday()

        # 숫자를 요일 이름으로 변환
        days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
        day_name = days[day_of_week]

        return day_name

    def return_specific_data(self, column, table_name, condition=None, type=1):
        """특정 열 데이터만 반환합니다."""
        c = self.start_conn()

        query = f"SELECT {column} FROM {table_name}"
        if condition is not None:
            query += f" WHERE {condition}"

        c.execute(query)
        r_data = c.fetchall()
        # print('데이터', r_data)

        if type == 1:
            return r_data[0][0]
        return r_data

    def return_user_atd_info(self, user_id, year_month):
        c = self.start_conn()
        user_no = self.find_no(user_id=user_id)  # 유저 아이디 반환

        query = f"select * from tb_atd where user_no = {user_no} and atd_date like '%{year_month}%' order by atd_date desc"
        c.execute(query)
        r_data = c.fetchall()

        return r_data

    def return_user_atd_month(self, user_id):
        """유저가 출근한 월들만 리스트로 반환"""
        user_no = self.find_no(user_id)  # 유저 번호 반환
        result = self.return_specific_data(column='atd_date', table_name='tb_atd', condition=f'user_no={user_no}',
                                           type=2)  # 유저 출근 날들 반환

        result = [date[0][:7] for date in result]  # 출근 년도 - 월수만 반환
        unique_result = []
        [unique_result.append(x) for x in result if x not in unique_result]  # 그 중 중복값 제거

        sorted_dates = sorted(unique_result)
        reversed_lst = sorted_dates[::-1]
        return reversed_lst

    def return_user_atd_summary(self, user_id):
        # 유저 이름
        con = f"user_id = '{user_id}'"  # 조건1
        user_name = self.return_specific_data(column='user_name', table_name='tb_user', condition=con)

        # 현재 년-월
        current_year_month = self.return_datetime(type='year_month')
        current_date = self.return_datetime(type='c_date')

        # 유저 번호
        user_no = self.find_no(user_id)

        # 출근일수
        con2 = f"user_no = {user_no} and atd_date like '%{current_year_month}%'"  # 조건2
        user_atd_day = self.return_specific_data(column='count(*)', table_name='tb_atd',
                                                 condition=con2, type=1)
        # 근태율 계산 = (현재 달 출근일 / 현재 달 날짜) * 100
        atd_per = round((int(user_atd_day) / int(current_date)) * 100, 2)
        absent_day = int(current_date) - int(user_atd_day)
        text = f'{user_name}님의 {current_year_month[-2:]}월 출근일수는 {user_atd_day}일, 근태율은 {atd_per}%입니다.'

        return text, user_atd_day, atd_per, absent_day

    # 팀별 근태율 리턴
    def return_team_atd_per_for_table(self, dept_name):
        team_member = self.select_dept(dept_name)
        per_list = list()

        for mem in team_member:
            user_id = mem[1]
            result = self.return_user_atd_summary(user_id)
            atd_per = result[2]
            per_list.append(atd_per)

        per_mean = sum(per_list) / len(per_list)
        return round(per_mean, 2)

    # 출근 여부 확인
    def clock_in_check(self, user_no, day_date):
        c = self.start_conn()
        check_query = f"select atd_start from tb_atd join tb_user on tb_atd.user_no = tb_user.user_no " \
                      f"where tb_atd.user_no = '{user_no}' and tb_atd.atd_date = '{day_date}'"
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

    # 부서명, 부서코드, 부서인원수 리턴해주기
    def info_dept(self):
        c = self.start_conn()
        dept_query = "select tb_dept.dept_id, tb_dept.dept_name, count(*) from tb_dept " \
                     "join tb_user on tb_dept.dept_id = tb_user.dept_id group by tb_dept.dept_id, tb_dept.dept_name"
        c.execute(dept_query)
        data = c.fetchall()
        self.end_conn()
        return data

    # 선택한 부서별 사원만 리스트 담아서 리턴
    def select_dept(self, dept):
        empolyee_list = list()
        c = self.start_conn()
        empolyee_query = "select tb_user.user_name, tb_user.user_id, tb_dept.dept_name from tb_user join tb_dept on tb_user.dept_id = tb_dept.dept_id " \
                         f"where tb_dept.dept_name = '{dept}'"

        c.execute(empolyee_query)
        datas = c.fetchall()
        for data in datas:
            empolyee_list.append(data)

        return empolyee_list

    # DB에서 아이디 / 패스워드 검증
    def check_id_pw(self, user_id):
        c = self.start_conn()
        check_query = f"select user_pw from tb_user where user_id = '{user_id}'"
        c.execute(check_query)
        pw = c.fetchone()

        if pw == None:
            return False  # 등록된 아이디 없음
        else:
            return pw[0]

    # 관리자 사원 등록 아이디 중복검사
    def id_duple_check(self, user_id):
        c = self.start_conn()
        query = f"select * from tb_user where user_id = '{user_id}'"
        c.execute(query)
        result = c.fetchone()
        if result != None:
            return False  # 중복된 아이디
        else:
            return True  # 중복 통과

    # 신규 사원 등록
    def save_newbie(self, newbie_name, newbie_id, newbie_pw, dept_id, join_date):
        c = self.start_conn()
        add_query = "insert into tb_user (user_name, user_id, user_pw, dept_id, user_join_date) values " \
                    f"('{newbie_name}', '{newbie_id}', '{newbie_pw}', '{dept_id}', '{join_date}')"
        c.execute(add_query)
        self.commit_db()
        self.end_conn()

    # 사원 삭제
    def delete_empolyee(self, emp_id):
        c = self.start_conn()
        del_query = f"delete from tb_user where user_id = '{emp_id}'"
        c.execute(del_query)
        self.commit_db()
        self.end_conn()

    # 퇴근 기록 DB 저장 코드
    def leave_workplace(self, user_id, day_date, time_date):
        user_no = self.find_no(user_id)
        c = self.start_conn()
        leave_query = f"update tb_atd set atd_end = 1, atd_leave = '{time_date}' " \
                      f"where user_no = '{user_no}' and atd_date = '{day_date}' and atd_end = 0"
        c.execute(leave_query)
        self.commit_db()
        self.end_conn()

    # tb_user 정보 가져오기
    def get_user_data(self, user_id):
        c = self.start_conn()
        find_query = f"select * from tb_user where user_id = '{user_id}'"
        c.execute(find_query)
        user_data = c.fetchone()
        return user_data

    def get_current_pw(self, user_id):
        c = self.start_conn()
        find_query = f"select user_pw from tb_user where user_id = '{user_id}'"
        c.execute(find_query)
        user_pw = c.fetchone()
        return user_pw[0]

    def save_new_pw(self, user_id, new_pw):
        c = self.start_conn()
        update_query = f"update tb_user set user_pw = '{new_pw}' where user_id = '{user_id}'"
        c.execute(update_query)
        self.commit_db()
        self.end_conn()

    def update_dept_id(self, user_id, dept_id):
        c = self.start_conn()
        update_query = f"update tb_user set dept_id = '{dept_id}' where user_id = '{user_id}'"
        c.execute(update_query)
        self.commit_db()
        self.end_conn()

    # 출결 임의 삽입 함수
    def test(self, date):
        c = self.start_conn()
        add_query = "insert into tb_atd (atd_date, atd_time, atd_start, atd_end, atd_type, user_no, atd_leave) values " \
                    f"('{date}', '{'08:50:30'}', '{1}', '{1}', '{'face'}','{2}', '{'18:10:10'}' )"
        c.execute(add_query)
        self.commit_db()
        self.end_conn()

    # 유저의 연도별 근태 일수 리턴
    def return_user_atd_per_year(self, user_id):
        month_list = [f'2023-{n:02}' for n in range(1, 12 + 1)]
        month_day_list = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        user_no = self.find_no(user_id=user_id)
        user_join_date = self.return_specific_data(column='user_join_date', table_name='tb_user', condition=f"user_id='{user_id}'")
        start_month = datetime.strptime(user_join_date, '%Y-%m-%d')
        start_month = start_month.month
        current_time = datetime.now()
        current_month = current_time.month

        atd_per_list = list()
        for month in range(start_month, current_month + 1):

            con = f"user_no = {user_no} and atd_date like '%2023-{month:02}%'"  # 조건2
            user_atd_day = self.return_specific_data(column='count(*)', table_name='tb_atd',
                                                     condition=con, type=1)

            # 근태율 계산 = (해당 달 출근일 / 해당 달 날짜) * 100
            atd_per = round(int(user_atd_day) / int(month_day_list[month]) * 100)
            atd_per_list.append(atd_per)
        month_list = [f'{i}월' for i in range(start_month, current_month+1)]
        return month_list, atd_per_list

    # 팀 이름과 팀원 수를 리턴함
    def count_dept_emp(self):
        c = self.start_conn()
        count_query = "select tb_dept.dept_name, count(tb_user.*) as count_emp from tb_user " \
                      "join tb_dept on tb_user.dept_id = tb_dept.dept_id " \
                      "group by tb_dept.dept_name"
        c.execute(count_query)
        data = c.fetchall()
        self.end_conn()

        return data

    # 관리자 팀별 근태율 확인하기 위한 그래프위한 데이터 리턴
    def return_team_atd_per(self, type='current'):
        dept_dict = dict()
        month_dict = {f"{n}월": 0 for n in range(1, 13)}  # 월 리스트
        current_month = datetime.now().month

        attendance_sum_by_dept = {dept: month_dict.copy() for dept in self.find_dept()}  # 각 부서별 월별 근태율 누적값
        attendance_count_by_dept = {dept: month_dict.copy() for dept in self.find_dept()}  # 각 부서별 월별 근무한 사람의 수

        depts = self.find_dept()  # 부서 리턴
        for dept in depts:  # 부서 for문
            mems = self.select_dept(dept)  # 부서에 속한 멤버들 가져오기
            for mem in mems:  # 멤버들 for문 돌리기
                m_list, atd_per = self.return_user_atd_per_year(mem[1])  # 멤버들의 출근달, 출근율 리스트로 가져오기
                for month, percentage in zip(m_list, atd_per):
                    attendance_sum_by_dept[dept][month] += percentage  # 누적 근태율 합산
                    attendance_count_by_dept[dept][month] += 1  # 해당 월에 근무한 사람의 수 증가

        # 평균 근태율 계산
        avg_attendance_by_dept = {dept: {} for dept in depts}
        avg_attendance_by_dept_for_graph = {}
        for dept in depts:
            avg_attendance_by_dept_for_graph[dept] = {}
            for month in month_dict.keys():
                if attendance_count_by_dept[dept][month] > 0:
                    avg = attendance_sum_by_dept[dept][month] / attendance_count_by_dept[dept][month]
                    avg_attendance_by_dept[dept][month] = round(avg, 2)  # 소수 두 자리까지 반올림
                    avg_attendance_by_dept_for_graph[dept][month] = round(avg, 2)

        # 리턴값
        # print(avg_attendance_by_dept_for_graph)
        currrent_values_by_dept = {dept: avg_attendance_by_dept[dept][f"{current_month}월"] for dept in depts} # 해당 달 근태율 계산
        if type == 'all':
            return avg_attendance_by_dept
        if type == 'graph':
            return avg_attendance_by_dept_for_graph
        return currrent_values_by_dept



# if __name__ == '__main__':
#     db_conn = DBconnect(controller=None)
#     data = db_conn.count_dept_emp()
#     print(data)
#     for team, member in data:
#         team_list.append(team)
#         memeber_list.append(member)
#     print(team_list, memeber_list)


    # 출결 임의 삽입
    # date = 31
    # date_list = [f'2023-07-{n:02}' for n in range(1, date + 1)]
    # for i in range(1, date+1):
    #     db_conn.test(date_list[i-1])
