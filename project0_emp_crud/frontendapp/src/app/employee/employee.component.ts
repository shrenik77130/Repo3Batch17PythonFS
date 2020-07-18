import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { EmployeeService } from '../services/employee.service';
import { Employee } from '../common/employee';

@Component({
  selector: 'app-employee',
  templateUrl: './employee.component.html',
  styleUrls: ['./employee.component.css']
})
export class EmployeeComponent implements OnInit {

  private indexUrl:string = "http://localhost:8000/";
  private result:string;
  private emparray:Employee[]=[];
  private empObject:Employee = new Employee();

  constructor(private http:HttpClient,private empservice:EmployeeService) { }

  ngOnInit() {
  }

  requestaBak():void{
    this.http.get(this.indexUrl).subscribe(data => this.result=data['data']);
  }

  getEmployees(){

    this.empservice.getAllEmployeesFromBackend().subscribe(
      (data)=>{
        console.log(data["employees"]);

        let arraydata = Object.keys(data["employees"]);
        for(var key of arraydata)
        {
         // console.log(key + "===>" + data["employees"][key]["empid"]);

          this.emparray.push(
            new Employee(
              data["employees"][key]["empid"],
              data["employees"][key]["fullname"],
              data["employees"][key]["gender"],
              data["employees"][key]["location"],
              data["employees"][key]["projectleader"],
              data["employees"][key]["projectcost"]
            )
          );
        }

      }
    );

  }

  submitEmpRecord(){
    console.log(this.empObject);
    this.empservice.insertEmpRecord(this.empObject);
  }

}
