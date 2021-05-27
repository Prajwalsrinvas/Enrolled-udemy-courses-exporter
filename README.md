# Enrolled Udemy courses exporter

## Used to get an excel file containing enrolled udemy courses data

### Getting Access token

Access token is required to get the list of enrolled courses in udemy account.

- Login to your udemy account
- Open console in devtools (ctrl+shift+i -> console tab)
- Paste this
```javascript
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}
getCookie('access_token')
```
