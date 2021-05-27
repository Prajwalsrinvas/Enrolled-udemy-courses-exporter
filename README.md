# Enrolled Udemy courses exporter

## Used to get an excel file containing enrolled udemy courses data

### Demonstration



https://user-images.githubusercontent.com/24704548/119854098-693df100-bf2e-11eb-8fa4-d07edc537b0f.mp4




### Getting Access token

Access token is required to get the list of enrolled courses in udemy account.

- Login to your udemy account.
- Open console in devtools (ctrl+shift+i -> console tab).
- Paste this.
```javascript
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}
getCookie('access_token')
```

![Get access token](https://github.com/Prajwalsrinvas/Enrolled-udemy-courses-exporter/blob/main/screenshots/1.console.png)

- Copy the string which is returned.This is your access token.

### Streamlit webapp 

- Go to [this](https://udemy-export.herokuapp.com/) site.
![Homepage](https://github.com/Prajwalsrinvas/Enrolled-udemy-courses-exporter/blob/main/screenshots/2.homepage.png)
- Paste access token in the box and wait till all course information is retrieved.
- First few rows are displayed just to get an idea of how the data is formatted.
- An Excel sheet containing all course information can be downloaded by clicking the download button.

![Streamlit app](https://github.com/Prajwalsrinvas/Enrolled-udemy-courses-exporter/blob/main/screenshots/3.webapp.png)
