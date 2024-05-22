var dt=new Date();
var month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
function display()
{
    var today = new Date();
    dt.setDate(1);



    
    document.getElementById("month").innerHTML=month[dt.getMonth()];
    document.getElementById("date").innerHTML=dt.getFullYear();

    var end_date= new Date(
        dt.getFullYear(),
        dt.getMonth()+1,
        0
    ).getDate();

    // console.log(end_date);

    var prev_date= new Date(
        dt.getFullYear(),
        dt.getMonth(),
        0
    ).getDate();
    // console.log(prev_date);
 



    var day=dt.getDay();
    // console.log(day);
    var cell="";
    if(day>0)
    {
        for(var x=day-1;x>0;x--)
        {
            cell+="<div class='prev-days'>"+(prev_date-x+1)+"</div>";
        }
    }
    else
    {
        for(x=5;x>=0;x--)
        {
            cell+="<div class='prev-days'>"+(prev_date-x)+"</div>";
        }
    }
    for(x=1;x<=end_date;x++)
    {
        if(x==today.getDate() && dt.getMonth()== today.getMonth() && dt.getFullYear()== today.getFullYear())
         cell+="<div class='today'>"+x+"</div>";
        else
        cell+="<div onclick='load_event(dt.getMonth(),dt.getFullYear())' >"+x+"</div>";
    }

    {
        var end_day = new Date(
            dt.getFullYear(),
            dt.getMonth()+1,
            0 
        ).getDay();
        if(end_day>0)
        {  var k=1;
            while(end_day<=6)
            {
                cell+="<div class='next-days'>"+k+"</div>";
                end_day++;
                k++;
            }
        }

        // document.getElementsByClassName("details")[0].innerHTML=today.toDateString();
    }



    document.getElementsByClassName("days")[0].innerHTML=cell;
}

function move_month(p)
{
    if (p=="prev")
    {
        dt.setMonth(dt.getMonth()-1);
    }
    else
    {
        dt.setMonth(dt.getMonth()+1);
    }
    display();
}

// function load_event(m,y)
// {
//    document.getElementsByClassName("details")[0].innerHTML=" "+month[m]+" "+y;

// }