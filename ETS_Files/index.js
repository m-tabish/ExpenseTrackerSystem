import {initializeApp} from "https://www.gstatic.com/firebasejs/9.15.0/firebase-app.js"
import {getDatabase,ref,push} from 'https://www.gstatic.com/firebasejs/9.15.0/firebase-database.js'

const appSettings = {
    databaseURL: 'https://console.firebase.google.com/project/prism-office-scanner/database/prism-office-scanner-default-rtdb/data/~2F'

}

const app = initializeApp(appSettings)
const database = getDatabase(app)
const shoppingListInDB = ref(database, "shoppingList")
const inputFieldEl = document.getElementById("input-field");
const addButtonEl = document.getElementById("add-button");

addButtonEl.addEventListener("click", function(){
    let inputValue =  inputFieldEl.value
    push(shoppingListInDB, inputValue)
    console.log(inputFieldEl.value)
}
)
