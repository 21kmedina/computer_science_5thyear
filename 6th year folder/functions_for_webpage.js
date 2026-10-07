
function update_user_name_btn(){
//get the value from the user input
let user_name_input = document.getElementById('user_name').value;
//update the span tag with the user input
document.getElementById('user_name_place_holder').innerHTML =
user_name_input;
}



function calculate_mean(){
//Get the user data  
let data_from_user = document.getElementById('user_dataset_1').value;
//split string data_from_user to list
let data_in_list = data_from_user.split(',')
//set up our variables
let total = 0
let num_items = 0
//iterate through the list to get the total
for (let temp of data_in_list){
//input is text so we need to cast to float
total = total + parseFloat(temp);
} 
//get the number of items in the list
num_items = data_in_list.length;
//calculate the average
let average = total/num_items
return average
}
function calculate_mean_btn(){
document.getElementById('user_dataset_1_placeholder').innerHTML = 
calculate_mean();
}
document.getElementById('user_name_place_holder').innerHTML = 
user_name_input;



function calculate_median(){
let data_from_user = document.getElementById('user_dataset_1').value;
let data_in_list = data_from_user.split(',')
data_in_list.sort();
///if the list of data is an odd number:
if (data_in_list.length % 2 != 0){
    ind= parseFloat(Math.floor(data_in_list.length/2))
    index=data_in_list[ind]
}

///if lst is odd
else if (data_in_list.length % 2 ==0){
///paresfloat converts the data from lst which is a string into a interger
let mid1= parseFloat(Math.floor(data_in_list.length/2))
let mid2=parseFloat(data_in_list.length/2)-1
index=mid1/mid2
        
 }

    return index
}
function calculate_median_btn(){
document.getElementById('user_dataset_1_placeholder_median').innerHTML = 
calculate_median();
}
document.getElementById('user_name_place_holder_median').innerHTML = 
user_dataset_1;




function calculate_range(){
    let data_from_user = document.getElementById('user_dataset_1').value;
    let data_in_list = data_from_user.split(',')
    data_in_list.sort();
    range=Math.max(data_in_list)-Math.min(data_in_list    
    )
    return range
}
///btn for calculate range
function calculate_range_btn(){
document.getElementById('user_dataset_1_placeholder_median').innerHTML=
calculate_range();
}
document.getElementById('user_dataset_1_placeholder_median').innerHTML = 
user_name_input;