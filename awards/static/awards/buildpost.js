buildPost()

function buildPost() {
    var wrapper = document.getElementById('Post-wrapper')
    var url = 'http://127.0.0.1:8000/api/post-list/'

    fetch(url)
    .then((res) => res.json())
    .then(function(data){
       console.log(data)
       var list = data

       for (let i in list) {
        let awards = `
            <div class="col-md-6 col-lg-4">
                <div class="card my-2">
                    <img style='height: 250px;object-fit:cover;' src="${list[i].image}" class="card-img-top" alt="photo image">
                    <div class="card-body">
                        <p class="card-text">Title: ${list[i].title}</p>
                    </div>
                    <a href="detail/1/" class="btn btn-outline-dark btn-sm view-btn">view</a>
                </div>
            </div>
        `
        wrapper.innerHTML += awards
    }
})
}