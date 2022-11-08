

const addStudent = () => {

    const username = document.getElementById('username').value
    const email = document.getElementById('email').value

    axios({
        method: 'POST',
        url: '/student/',
        data: {
            name: username,
            email: email,
        }
    }).then(function (response) {
        console.log(response.data)
    })
}