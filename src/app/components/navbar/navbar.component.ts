import { Component, OnInit, HostListener } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { DplayerService } from 'src/app/services/dplayer.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {

  classApplied = false;
  dropActive = false;
  notFound = false;
  conver:any;

  toggleClass() {
    this.classApplied = !this.classApplied;
  }
  DropDowmMenu(){
    this.dropActive = !this.dropActive;
  }

  constructor( private router: Router,
     public dplayer: DplayerService,
     private activatedRoute:ActivatedRoute) { }

  ngOnInit(): void {

    // this.activatedRoute.params.subscribe( params => {
    //   console.log("params",params);
    // })

  }

  header_variable = false;
  @HostListener("document:scroll")
  scrollfunction(){
    if(document.body.scrollTop > 0 || document.documentElement.scrollTop > 0){
      this.header_variable=true;
    }
    else{
      this.header_variable=false;
    }
  }

  findprofile( text:string ){
    text = text.trim();
    if(text.length === 0){
      return;
    }else{
      this.activatedRoute.params.subscribe( params => {
        console.log("params",params);
        //llamar al servicio
      })
      this.dplayer.getDplayer().subscribe(resp => {
    //  console.log(resp);
        // this.conver=resp
        this.dplayer.conver2 = resp
        console.log(this.dplayer.conver2[0])  
        this.dplayer.WZ = this.dplayer.conver2[0].warzone
        this.dplayer.BR = this.dplayer.conver2[0].battle
        console.log(this.dplayer.WZ)
        console.log(this.dplayer.BR)
      })
      this.router.navigate(['/profile', text]);
      this.toggleClass()
    }
  }

  getUser(){
    this.dplayer.getDplayer().subscribe(resp => {
      console.log(resp)
      this.conver=resp;
    }, (err: any) =>{
      console.error(err);
      this.notFound = true;
    });
  }

}
