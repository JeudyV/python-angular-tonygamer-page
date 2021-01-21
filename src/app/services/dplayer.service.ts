import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IDataPlayer } from '../interfaces/dataplayer';

@Injectable({
  providedIn: 'root'
})
export class DplayerService {

  private baseUrl = 'http://127.0.0.1:5000'
  conver2:any = ' ';
  WZ:any = ' ';
  BR:any = ' ';

  constructor( private http: HttpClient ) { }

  getDplayer(){
    return this.http.get(`${ this.baseUrl }/List_price`)
  } 
  getSearchPlayer( text:string ){

    // return this.http.get(`${ this.baseUrl }/search/player/${ text }`)

  }
}
