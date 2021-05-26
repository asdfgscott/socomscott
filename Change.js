var denomination = [20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01];
//var change =  parseFloat(prompt("What is your change?"));

function math(change){
  var x = change;
  var twentcount = 0, tencount = 0,fivecount = 0, onecount =0;
  while(x / 20 >= 1){
    x -= 20;
    twentcount ++;
  }
  while(x / 10 >= 1){
    x -= 10;
    tencount ++;
  }
  while(x / 5 >= 1){
    x -=5;
    fivecount ++;
  }
  while(x / 1 >= 1){
    x -= 1;
    onecount ++;
  }
  process.stdout.write("We need " + twentcount + " x $20 \n");
  process.stdout.write("We need " + tencount + " x $10 \n");
  process.stdout.write("We need " + onecount + " x $1 \n");
}


function mathv2(change){
  var x = change;
  var position = 0;
  var counter = 0;

  while( x != 0){
    if(x >= denomination[position]){
      while(x/denomination[position] >= 1){
        x -= denomination[position];
        x = x.toFixed(2);
        //process.stdout.write(x + "\n")
        counter ++;
      }
      process.stdout.write("We need " + counter + " x $" + denomination[position] + "\n");
      counter = 0;
      position ++;
    }
    else{
      position ++
    }
  }
  process.stdout.write("Done.")
}
  
  


const args = process.argv.slice(2);
//math(args[0]);
mathv2(args[0]);