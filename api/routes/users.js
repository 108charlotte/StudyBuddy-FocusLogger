const express = require("express")
const router = express.Router()

router.use(logger)

router.get("/", (req, res) => {
    res.send("User list")
})

// static routes should go above dynamic routes, otherwise new would be viewed as an id
router.get("/new", (req, res) => {
    res.send("User New Form")
})

router.post("/", (req, res) => {
    res.send("Create User")
})

router.route("/:id").get((req,res) => {
    console.log(req.user)
    res.send("Get User with ID ${req.params.id}")
}).put((req,res) => {
    res.send("Update User with ID ${req.params.id}")
}).delete((req,res) => {
    res.send("Delete User with ID ${req.params.id}")
})

const users = [{ name: "Kyle" }, { name: "Sally" }]

// param: middleware: between request & response to user
router.param("id", (req, res, next, id) => {
    req.user = users[id]
    next()
})


function logger(req, res, next) {
    console.log(req.originalUrl)
    next()
}

module.exports = router