# Enrolled Udemy courses exporter

## Used to get an excel file containing enrolled udemy courses data

## Demonstration



https://user-images.githubusercontent.com/24704548/119854098-693df100-bf2e-11eb-8fa4-d07edc537b0f.mp4




## Getting Access token

Access token is required to get the list of enrolled courses in udemy account.

1. Login to your udemy account.
2. Open console in devtools (ctrl+shift+i ---> console tab).
3. Copy the JavaScript snippet given below and paste it into the console window.
```javascript
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}
getCookie('access_token')
```
4. Copy the string which is returned.This is your access token.

![Get access token](https://github.com/Prajwalsrinvas/Enrolled-udemy-courses-exporter/blob/main/screenshots/1.console.png)

## Streamlit webapp 

![Homepage](https://github.com/Prajwalsrinvas/Enrolled-udemy-courses-exporter/blob/main/screenshots/2.homepage.png)

1. Go to [this](https://udemy-export.herokuapp.com/) site.
2. Paste access token in the box and wait till all course information is retrieved.
3. First few rows are displayed just to get an idea of how the data is formatted.
4. An Excel sheet containing all course information can be downloaded by clicking the download button.

![Streamlit app](https://github.com/Prajwalsrinvas/Enrolled-udemy-courses-exporter/blob/main/screenshots/3.webapp.png)
