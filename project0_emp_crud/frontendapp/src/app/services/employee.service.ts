import { Injectable } from '@angular/core';
import { Employee } from '../common/employee';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map, catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class EmployeeService {

  private empUrl:string = "http://localhost:8000/getall/";
  private empSaveUrl:string = "http://localhost:8000/empsave/";
  private emprecords:Employee[];
  private apirecords;

  constructor(private httpClient:HttpClient) { }

  getAllEmployeesFromBackend(){

    // Observable Function...   returns the data calling function asynchronously
    return this.httpClient.get(this.empUrl).pipe(
      map(  (data:Employee[])=>{
        return data;
      }),catchError(error=>{return error})
    );
  }

  insertEmpRecord(empObject){
    console.log("in Emp Service, Emp Rec = "+ empObject);
    return this.httpClient.post(this.empSaveUrl,empObject,{responseType:'json'}).subscribe(data=> console.log("Success",data),
    error=> console.log("Error!",error)
);;
  }
}

interface GetResponseEmployee{
  employees:{
    employees:Employee[];
  }
}

