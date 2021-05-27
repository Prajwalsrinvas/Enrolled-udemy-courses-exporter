import requests
import pandas as pd
import time
import streamlit as st
import base64
import io

st.set_page_config(page_title='Udemy Export', page_icon='💡', layout='wide')

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown('<center><h1 style="color:#008080;"><u>Enrolled Udemy courses exporter</u></h1></center>',
            unsafe_allow_html=True)
ACCESS_TOKEN = st.text_input("Enter access_token:")
val = False


def get_json_data(page_num):
    headers = {
        'authority': 'www.udemy.com',
        'authorization': f'Bearer {ACCESS_TOKEN}',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'x-udemy-authorization':
        f'Bearer {ACCESS_TOKEN}',
    }

    params = (
        ('ordering', '-enroll_time'),
        ('fields^/[course^/]',
         '^@min,visible_instructors,image_240x135,favorite_time,archive_time,completion_ratio,last_accessed_time,enrollment_time,is_practice_test_course,features,num_collections,published_title,is_private,is_published,buyable_object_type'
         ),
        ('fields^/[user^/]', '^@min,job_title'),
        ('page', str(page_num)),
        ('page_size', '100'),
        ('is_archived', 'false'),
    )

    response = requests.get(
        'https://www.udemy.com/api-2.0/users/me/subscribed-courses/',
        headers=headers,
        params=params)
    return response.json()


df = pd.DataFrame(columns=[
    'Course Name', 'Price', 'Instructor(s)', 'Course URL', 'Instructor(s) URL'
])


def main(ACCESS_TOKEN):
    last_page_reached = False
    total_courses = 0
    if ACCESS_TOKEN:
        json_data = get_json_data(1)
        if json_data.get('detail', None) == 'You do not have permission to perform this action.':
            st.markdown('<h4 style="color:red">Wrong Access token!</h4>',
                        unsafe_allow_html=True)
        else:
            st.write('Extracting enrolled courses data!')
            curr_page = 1
            while True:
                json_data = get_json_data(curr_page)

                if json_data.get('detail', None) == 'Invalid page.':
                    st.write('Extraction done!')
                    last_page_reached = True
                    break

                total_courses += len(json_data["results"])
                st.write(
                    f'Extracted {total_courses} courses data{"."*curr_page}')

                for course in json_data['results']:
                    course_name = course['title'].strip()
                    price = course['price']
                    instructor = " | ".join(
                        [i['title'] for i in course['visible_instructors']])
                    course_url = f"udemy.com{course['url'].replace('/learn/','')}"
                    instructor_url = " | ".join(
                        [f"udemy.com{i['url']}" for i in course['visible_instructors']])

                    index = len(df)
                    df.loc[index] = [
                        course_name, price, instructor, course_url, instructor_url
                    ]
                curr_page += 1
                time.sleep(5)

            sentence = f"Total Enrolled Courses: {len(df)}"
            st.markdown(
                f'<h3 style="color:#008080;">{sentence}</h3>', unsafe_allow_html=True)

            if last_page_reached:
                towrite = io.BytesIO()
                downloaded_file = df.to_excel(
                    towrite, encoding='utf-8', index=False, header=True)
                towrite.seek(0)  # reset pointer
                b64 = base64.b64encode(towrite.read()).decode()  # some strings
                linko = f'<a style="color:black" href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="udemy_enrolled_courses.xlsx">Download enrolled courses data as an excel sheet</a>'
                button = f'<center><button style="background-color: #4CAF50; border-radius: 4px; font-size: 20px;">{linko}</button></center>'
                st.markdown(button, unsafe_allow_html=True)
                st.write('First few rows:\n')
                st.table(df[:10])


if ACCESS_TOKEN:
    if len(str(ACCESS_TOKEN)) == 40:
        main(ACCESS_TOKEN)
    else:
        st.markdown('<h4 style="color:red">Wrong Access token!</h4>',
                    unsafe_allow_html=True)
