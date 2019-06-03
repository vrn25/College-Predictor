var opt=new Array(6);
var branchp=9;

for (var i = 0; i < opt.length; i++) {
  opt[i] = new Array(branchp);
}

    opt[0][0]="Indian Institute of Technology Bombay";
    opt[1][0]="Indian Institute of Technology Delhi";
    opt[2][0]="National Institute of Technology Surathkal";
    opt[3][0]="National Institute of Technology Trichy";
    opt[4][0]="Indian Institute of Information Technology Allahabad";
    opt[5][0]="Indian Institute of Information Technology Delhi";

for(var i=0;i<6;i++){
    opt[i][1]="Aerospace Engineering";
    opt[i][2]="Chemical Engineering";
    opt[i][3]="Civil Engineering";
    opt[i][4]="Computer Science and Engineering";
    opt[i][5]="Electrical Engineering";
    opt[i][6]="Electronics and Communication";
    opt[i][7]="Information Technology";
    opt[i][8]="Mechanical Engineering";
}
var html1_before=(document.getElementById("lstBox1")).innerHTML;


function update1()
        {
            var collegename=document.getElementById("college_name");
            var choices=document.getElementById("lstBox1");
            var selected=collegename.value;
            var html='<option disabled selected="selected">College Choices</option>';
            var b=(document.getElementById("branch_name")).value
            if(selected==="10000"){
                
                if(b==="100001"){
                
                    choices.innerHTML=html1_before;
                    console.log(html1_before);
                }
                else{
                    
                    var aero=[];
    for(var i=0;i<opt.length;i++){
        if(i===0||i===1){
            aero.push( opt[i][0] + ', ' + opt[i][1] );
        }
    }
    var chem=[];
    for(var i=0;i<opt.length;i++){
        if(i!==4 && i!==5){
            chem.push( opt[i][0] + ', ' + opt[i][2] );
        }
    }
    var civ=[];
    for(var i=0;i<opt.length;i++){
        if(i!==4 && i!==5){
            civ.push( opt[i][0] + ', ' + opt[i][3] );
        }
    }
    var comp=[];
    for(var i=0;i<opt.length;i++){
        
            comp.push( opt[i][0] + ', ' + opt[i][4] );
        
    }
    var ee=[];
    for(var i=0;i<opt.length;i++){
        
            ee.push( opt[i][0] + ', ' + opt[i][5] );
        
    }
    var ec=[];
    for(var i=0;i<opt.length;i++){
        
            ec.push( opt[i][0] + ', ' + opt[i][6] );
        
    }
    var it=[];
    for(var i=0;i<opt.length;i++){
        if(i!==0 && i!==1){
            it.push( opt[i][0] + ', ' + opt[i][7] );
        }
    }
    var me=[];
    for(var i=0;i<opt.length;i++){
        if(i!==4 && i!==5){
            me.push( opt[i][0] + ', ' + opt[i][8] );
        }
    }
                    
                if(b==="0"){    
                        for(var i=0; i < aero.length; i++)
                {
                    html+='<option>' + aero[i] + '</option>';
                }
                    }
                    else if(b==="1"){
                 for(var i=0; i < chem.length; i++)
                {
                    html+='<option>' + chem[i] + '</option>';
                }       
                    }
                    else if(b==="2"){
                 for(var i=0; i < civ.length; i++)
                {
                    html+='<option>' + civ[i] + '</option>';
                }       
                    }
                    else if(b==="3"){
                 for(var i=0; i < comp.length; i++)
                {
                    html+='<option>' + comp[i] + '</option>';
                }       
                    }
                    else if(b==="4"){
                 for(var i=0; i < ee.length; i++)
                {
                    html+='<option>' + ee[i] + '</option>';
                }       
                    }
                    else if(b==="5"){
                 for(var i=0; i < ec.length; i++)
                {
                    html+='<option>' + ec[i] + '</option>';
                }       
                    }
                    else if(b==="6"){
                 for(var i=0; i < it.length; i++)
                {
                    html+='<option>' + it[i] + '</option>';
                }       
                    }
                    else if(b==="7"){
                 for(var i=0; i < me.length; i++)
                {
                    html+='<option>' + me[i] + '</option>';
                }       
                    }
                choices.innerHTML=html;
                }
            }

            
    else{
            if((document.getElementById("branch_name")).value==="100001"){
            var iitb=[];
                
                for (var j=1; j<branchp ; j++){ 
                    if(j!==7){    
                    iitb.push( opt[0][0]+', '+opt[0][j] );   
                    }
            }
            
            var iitd=[];
                
                for (var j=1; j<branchp; j++){
                    
                    if(j!==7){    
                    iitd.push( opt[1][0]+', '+opt[1][j] );   
                    }
            }
            
            var nitk=[];
                
                for (var j=1; j<branchp; j++){
                    
                    if(j!==1){    
                    nitk.push( opt[2][0]+', '+opt[2][j] );   
                    }
            }
            
            var nitt=[];
                
                for (var j=1; j<branchp; j++){
                    
                    if(j!==1){    
                    nitt.push( opt[3][0]+', '+opt[3][j] );   
                    }
            }
            
            var iiita=[];
                
                for (var j=1; j<branchp; j++){
                    
                    if(j===4 || j===5 || j===6 || j===7){    
                    iiita.push( opt[4][0]+', '+opt[4][j] );   
                    }
            }
            
            var iiitd=[];
                
                for (var j=1; j<branchp; j++){
                    
                    if(j===4 || j===5 || j===6 || j===7){    
                    iiitd.push( opt[5][0]+', '+opt[5][j] );   
                    }
            }
            
            if(selected === "0")
            {
                for(var i=0; i < iitb.length; i++)
                {
                    html+='<option>' + iitb[i] + '</option>';
                }
            }
            else if(selected === "1")
            {
                for(var i=0; i < iitd.length; i++)
                {
                    html+='<option>' + iitd[i] + '</option>';
                }
            }
            else if(selected === "2")
            {
                for(var i=0; i < nitk.length; i++)
                {
                    html+='<option>' + nitk[i] + '</option>';
                }
            }
            else if(selected === "3")
            {
                for(var i=0; i < nitt.length; i++)
                {
                    html+='<option>' + nitt[i] + '</option>';
                }
            }
            else if(selected === "4")
            {
                for(var i=0; i < iiita.length; i++)
                {
                    html+='<option>' + iiita[i] + '</option>';
                }
            }
            else if(selected === "5")
            {
                for(var i=0; i < iiitd.length; i++)
                {
                    html+='<option>' + iiitd[i] + '</option>';
                }
            }
            
            choices.innerHTML=html;
        }
            else{
                var z=(document.getElementById("branch_name")).value;        
            
                if(z==="0"){
                    
                    var iitb=[];
            iitb.push( opt[0][z] + ', ' + opt[0][1] );
            
            var iitd=[];
            iitd.push( opt[1][z] + ', ' + opt[1][1] );
                    
                    if(selected==="0"){
                for(var i=0; i < iitb.length; i++)
                    {
                        html+='<option>' + iitb[i] + '</option>';
                    }    
                    }
                    else if(selected==="1"){
                     for(var i=0; i < iitd.length; i++)
                    {
                        html+='<option>' + iitd[i] + '</option>';
                    }   
                    }
                }
                else if(z==="1" || z==="2" || z==="7"){
                    
                    var iitb=[];
            iitb.push( opt[0][0] + ', ' + opt[0][Number(z)+1]);
            
            var iitd=[];
            iitd.push( opt[1][0] + ', ' + opt[1][Number(z)+1] );
                    
                    var nitk=[];
            nitk.push( opt[2][0] + ', ' + opt[2][Number(z)+1] );
            
            var nitt=[];
            nitt.push( opt[3][0] + ', ' + opt[3][Number(z)+1] );
                    
                    if(selected==="0"){
                        for(var i=0; i < iitb.length; i++)
                    {
                        html+='<option>' + iitb[i] + '</option>';
                    }
                    }
                    else if(selected==="1"){
                        for(var i=0; i < iitd.length; i++)
                    {
                        html+='<option>' + iitd[i] + '</option>';
                    }
                    }
                    else if(selected==="2"){
                        for(var i=0; i < nitk.length; i++)
                    {
                        html+='<option>' + nitk[i] + '</option>';
                    }
                    }
                    else if(selected==="3"){
                        for(var i=0; i < nitt.length; i++)
                    {
                        html+='<option>' + nitt[i] + '</option>';
                    }
                    }
                }
                else if(z==="3" || z==="4" || z==="5"){
                    
                    var iitb=[];
            iitb.push( opt[0][0] + ', ' + opt[0][Number(z)+1]);
            
            var iitd=[];
            iitd.push( opt[1][0] + ', ' + opt[1][Number(z)+1] );
                    
                    var nitk=[];
            nitk.push( opt[2][0] + ', ' + opt[2][Number(z)+1] );
                    
                    var nitt=[];
            nitt.push( opt[3][0] + ', ' + opt[3][Number(z)+1] );
                    
                   var iiita=[];
            iiita.push( opt[4][0] + ', ' + opt[4][Number(z)+1] );
                   
                    var iiitd=[];
            iiitd.push( opt[5][0] + ', ' + opt[5][Number(z)+1] );
                       
                    if(selected==="0"){
                     for(var i=0; i < iitb.length; i++)
                    {
                        html+='<option>' + iitb[i] + '</option>';
                    }   
                    }
                    else if(selected==="1"){
                     for(var i=0; i < iitd.length; i++)
                    {
                        html+='<option>' + iitd[i] + '</option>';
                    }   
                    }
                    else if(selected==="2"){
                     for(var i=0; i < nitk.length; i++)
                    {
                        html+='<option>' + nitk[i] + '</option>';
                    }   
                    }
                    else if(selected==="3"){
                     for(var i=0; i < nitt.length; i++)
                    {
                        html+='<option>' + nitt[i] + '</option>';
                    }   
                    }
                    else if(selected==="4"){
                     for(var i=0; i < iiita.length; i++)
                    {
                        html+='<option>' + iiita[i] + '</option>';
                    }   
                    }
                    else if(selected==="5"){
                     for(var i=0; i < iiitd.length; i++)
                    {
                        html+='<option>' + iiitd[i] + '</option>';
                    }   
                    }
                    
                }
                else if(z==="6"){
                    
                    var nitk=[];
            nitk.push( opt[2][0] + ', ' + opt[2][Number(z)+1] );
                    
                    var nitt=[];
            nitt.push( opt[3][0] + ', ' + opt[3][Number(z)+1] );
                    
                   var iiita=[];
            iiita.push( opt[4][0] + ', ' + opt[4][Number(z)+1] );
                   
                    var iiitd=[];
            iiitd.push( opt[5][0] + ', ' + opt[5][Number(z)+1] );
                    
                    if(selected==="2"){
                     for(var i=0; i < nitk.length; i++)
                    {
                        html+='<option>' + nitk[i] + '</option>';
                    }   
                    }
                    else if(selected==="3"){
                     for(var i=0; i < nitt.length; i++)
                    {
                        html+='<option>' + nitt[i] + '</option>';
                    }   
                    }
                    else if(selected==="4"){
                     for(var i=0; i < iiita.length; i++)
                    {
                        html+='<option>' + iiita[i] + '</option>';
                    }   
                    }
                    else if(selected==="5"){
                     for(var i=0; i < iiitd.length; i++)
                    {
                        html+='<option>' + iiitd[i] + '</option>';
                    }   
                    }
                }
                choices.innerHTML=html;
            }
        }
        }

function update2(){
    
            var branchname=document.getElementById("branch_name");
            var choices=document.getElementById("lstBox1");
            var selected=branchname.value;
            var html='<option disabled selected="selected">College Choices</option>';
            var c=(document.getElementById("college_name")).value
    
    if(selected==="100001"){
        
        if(c==="10000"){
        
            choices.innerHTML=html1_before;
        }
         else{
                
             var iitb=[];
                
                for (var j=1; j<branchp ; j++){ 
                    if(j!==7){    
                    iitb.push( opt[0][0]+', '+opt[0][j] );   
                    }
            }
            
            var iitd=[];
                
                for (var j=1; j<branchp; j++){
                    
                    if(j!==7){    
                    iitd.push( opt[1][0]+', '+opt[1][j] );   
                    }
            }
            
            var nitk=[];
                
                for (var j=1; j<branchp; j++){
                    
                    if(j!==1){    
                    nitk.push( opt[2][0]+', '+opt[2][j] );   
                    }
            }
            
            var nitt=[];
                
                for (var j=1; j<branchp; j++){
                    
                    if(j!==1){    
                    nitt.push( opt[3][0]+', '+opt[3][j] );   
                    }
            }
            
            var iiita=[];
                
                for (var j=1; j<branchp; j++){
                    
                    if(j===4 || j===5 || j===6 || j===7){    
                    iiita.push( opt[4][0]+', '+opt[4][j] );   
                    }
            }
            
            var iiitd=[];
                
                for (var j=1; j<branchp; j++){
                    
                    if(j===4 || j===5 || j===6 || j===7){    
                    iiitd.push( opt[5][0]+', '+opt[5][j] );   
                    }
            }
             if(c==="0"){
                 for(var i=0; i < iitb.length; i++)
                {
                    html+='<option>' + iitb[i] + '</option>';
                }
             }
             else if(c==="1"){
                 for(var i=0; i < iitd.length; i++)
                {
                    html+='<option>' + iitd[i] + '</option>';
                }
             }
             else if(c==="2"){
                 for(var i=0; i < nitk.length; i++)
                {
                    html+='<option>' + nitk[i] + '</option>';
                }
             }
             else if(c==="3"){
                 for(var i=0; i < nitt.length; i++)
                {
                    html+='<option>' + nitt[i] + '</option>';
                }
             }
             else if(c==="4"){
                 for(var i=0; i < iiita.length; i++)
                {
                    html+='<option>' + iiita[i] + '</option>';
                }
             }
             else if(c==="5"){
                 for(var i=0; i < iiitd.length; i++)
                {
                    html+='<option>' + iiitd[i] + '</option>';
                }
             }
             choices.innerHTML=html;
            }
    }
    else{
    
    if((document.getElementById("college_name")).value==="10000"){
    
        var aero=[];
    for(var i=0;i<opt.length;i++){
        if(i===0||i===1){
            aero.push( opt[i][0] + ', ' + opt[i][1] );
        }
    }
    var chem=[];
    for(var i=0;i<opt.length;i++){
        if(i!==4 && i!==5){
            chem.push( opt[i][0] + ', ' + opt[i][2] );
        }
    }
    var civ=[];
    for(var i=0;i<opt.length;i++){
        if(i!==4 && i!==5){
            civ.push( opt[i][0] + ', ' + opt[i][3] );
        }
    }
    var comp=[];
    for(var i=0;i<opt.length;i++){
        
            comp.push( opt[i][0] + ', ' + opt[i][4] );
        
    }
    var ee=[];
    for(var i=0;i<opt.length;i++){
        
            ee.push( opt[i][0] + ', ' + opt[i][5] );
        
    }
    var ec=[];
    for(var i=0;i<opt.length;i++){
        
            ec.push( opt[i][0] + ', ' + opt[i][6] );
        
    }
    var it=[];
    for(var i=0;i<opt.length;i++){
        if(i!==0 && i!==1){
            it.push( opt[i][0] + ', ' + opt[i][7] );
        }
    }
    var me=[];
    for(var i=0;i<opt.length;i++){
        if(i!==4 && i!==5){
            me.push( opt[i][0] + ', ' + opt[i][8] );
        }
    }
            
        if(selected === "0")
            {
                for(var i=0; i < aero.length; i++)
                {
                    html+='<option>' + aero[i] + '</option>';
                }
            }
        if(selected === "1")
            {
                for(var i=0; i < chem.length; i++)
                {
                    html+='<option>' + chem[i] + '</option>';
                }
            }
    if(selected === "2")
            {
                for(var i=0; i < civ.length; i++)
                {
                    html+='<option>' + civ[i] + '</option>';
                }
            }
    if(selected === "3")
            {
                for(var i=0; i < comp.length; i++)
                {
                    html+='<option>' + comp[i] + '</option>';
                }
            }
    if(selected === "4")
            {
                for(var i=0; i < ee.length; i++)
                {
                    html+='<option>' + ee[i] + '</option>';
                }
            }
    if(selected === "5")
            {
                for(var i=0; i < ec.length; i++)
                {
                    html+='<option>' + ec[i] + '</option>';
                }
            }
    if(selected === "6")
            {
                for(var i=0; i < it.length; i++)
                {
                    html+='<option>' + it[i] + '</option>';
                }
            }
    if(selected === "7")
            {
                for(var i=0; i < me.length; i++)
                {
                    html+='<option>' + me[i] + '</option>';
                }
            }
    
    choices.innerHTML=html;
        
    }
    
    else{
    
        var y=(document.getElementById("college_name")).value
        
    if(y==="0" || y==="1"){
            
        
        if(selected==="6"){
            
        }
        else{
                var aero=[];                    
        aero.push( opt[y][0] + ', ' + opt[y][1] );
        
            var chem=[];                    
        chem.push( opt[y][0] + ', ' + opt[y][2] );
            
            var civ=[];                    
        civ.push( opt[y][0] + ', ' + opt[y][3] );
            
            var comp=[];                    
        comp.push( opt[y][0] + ', ' + opt[y][4] );
            
            var ee=[];                    
        ee.push( opt[y][0] + ', ' + opt[y][5] );
            
            var ec=[];                    
        ec.push( opt[y][0] + ', ' + opt[y][6] );
            
            var me=[];                    
        me.push( opt[y][0] + ', ' + opt[y][8] );
            
            if(selected === "0")
            {
                for(var i=0; i < aero.length; i++)
                {
                    html+='<option>' + aero[i] + '</option>';
                }
            }
            if(selected === "1")
            {
                for(var i=0; i < chem.length; i++)
                {
                    html+='<option>' + chem[i] + '</option>';
                }
            }
            if(selected === "2")
            {
                for(var i=0; i < civ.length; i++)
                {
                    html+='<option>' + civ[i] + '</option>';
                }
            }
            if(selected === "3")
            {
                for(var i=0; i < comp.length; i++)
                {
                    html+='<option>' + comp[i] + '</option>';
                }
            }
            if(selected === "4")
            {
                for(var i=0; i < ee.length; i++)
                {
                    html+='<option>' + ee[i] + '</option>';
                }
            }
            if(selected === "5")
            {
                for(var i=0; i < ec.length; i++)
                {
                    html+='<option>' + ec[i] + '</option>';
                }
            }
            if(selected === "7")
            {
                for(var i=0; i < me.length; i++)
                {
                    html+='<option>' + me[i] + '</option>';
                }
            }
            
        }
        choices.innerHTML=html;
    }
        
        else if(y==="2" || y==="3"){
        
        
        if(selected==="0"){
            
        }
        else{        
            var chem=[];                    
        chem.push( opt[y][0] + ', ' + opt[y][2] );
            
            var civ=[];                    
        civ.push( opt[y][0] + ', ' + opt[y][3] );
            
            var comp=[];                    
        comp.push( opt[y][0] + ', ' + opt[y][4] );
            
            var ee=[];                    
        ee.push( opt[y][0] + ', ' + opt[y][5] );
            
            var ec=[];                    
        ec.push( opt[y][0] + ', ' + opt[y][6] );
            
            var it=[];                    
        it.push( opt[y][0] + ', ' + opt[y][7] );
            
            var me=[];                    
        me.push( opt[y][0] + ', ' + opt[y][8] );
            
            if(selected === "1")
            {
                for(var i=0; i < chem.length; i++)
                {
                    html+='<option>' + chem[i] + '</option>';
                }
            }
            if(selected === "2")
            {
                for(var i=0; i < civ.length; i++)
                {
                    html+='<option>' + civ[i] + '</option>';
                }
            }
            if(selected === "3")
            {
                for(var i=0; i < comp.length; i++)
                {
                    html+='<option>' + comp[i] + '</option>';
                }
            }
            if(selected === "4")
            {
                for(var i=0; i < ee.length; i++)
                {
                    html+='<option>' + ee[i] + '</option>';
                }
            }
            if(selected === "5")
            {
                for(var i=0; i < ec.length; i++)
                {
                    html+='<option>' + ec[i] + '</option>';
                }
            }
            if(selected === "6")
            {
                for(var i=0; i < it.length; i++)
                {
                    html+='<option>' + it[i] + '</option>';
                }
            }
            if(selected === "7")
            {
                for(var i=0; i < me.length; i++)
                {
                    html+='<option>' + me[i] + '</option>';
                }
            }
            
        }
        choices.innerHTML=html;
        }
        
        else if(y==="4" || y==="5"){
        
        if(selected==="0" || selected==="1" || selected==="2" || selected==="8"){
            
        }
        else{        
            var comp=[];                    
        comp.push( opt[y][0] + ', ' + opt[y][4] );
            
            var ee=[];                    
        ee.push( opt[y][0] + ', ' + opt[y][5] );
            
            var ec=[];                    
        ec.push( opt[y][0] + ', ' + opt[y][6] );
            
            var it=[];                    
        it.push( opt[y][0] + ', ' + opt[y][7] );
                        
            if(selected === "3")
            {
                for(var i=0; i < comp.length; i++)
                {
                    html+='<option>' + comp[i] + '</option>';
                }
            }
            if(selected === "4")
            {
                for(var i=0; i < ee.length; i++)
                {
                    html+='<option>' + ee[i] + '</option>';
                }
            }
            if(selected === "5")
            {
                for(var i=0; i < ec.length; i++)
                {
                    html+='<option>' + ec[i] + '</option>';
                }
            }
            if(selected === "6")
            {
                for(var i=0; i < it.length; i++)
                {
                    html+='<option>' + it[i] + '</option>';
                }
            }
        }
        choices.innerHTML=html;
        }
}
}
}