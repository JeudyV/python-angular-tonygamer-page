import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DplayerService } from 'src/app/services/dplayer.service';
import { IDataPlayer } from '../../interfaces/dataplayer';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
  notFound = false;
  user:any;

  constructor( public dplayer: DplayerService, private activatedRoute: ActivatedRoute){}

  ngOnInit(): void {
    // this.activatedRoute.params.subscribe( params => {
    //   console.log("profile params", params.text);
    //   //llamar al servicio
    //   this.dplayer.getSearchPlayer( params.text ).subscribe( resp =>{
    //     // console.log(resp)
    //   })
    // })

    this.dplayer.getDplayer().subscribe( resp => {
      console.log(resp);
    } )
    this.notFound = false;

    this.dplayer.getDplayer().subscribe(resp => {
      this.user = resp;
      console.log('prueba', this.user)
    })

  }


  getUser(){
    this.notFound = false;

    this.dplayer.getDplayer().subscribe(resp => {
      // this.user = resp;
      // console.log(user)
    }, (err: any) =>{
      console.error(err);
      this.notFound = true;
    });
  }

}
