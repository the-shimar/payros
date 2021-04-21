console.log('working')

$("#table2excel_button").click(function(){
    $("#table2excel").table2excel({
      // exclude CSS class
      exclude: ".noExl",
      name: "Salary",
      filename: "Salary_Exported", //do not include extension
      fileext: ".xlsx" // file extension
    }); 
  });