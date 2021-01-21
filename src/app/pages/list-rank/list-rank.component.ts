import { Component, OnInit } from '@angular/core';
import { DplayerService } from 'src/app/services/dplayer.service';

@Component({
  selector: 'app-list-rank',
  templateUrl: './list-rank.component.html',
  styleUrls: ['./list-rank.component.scss']
})
export class ListRankComponent implements OnInit {

  constructor( private dplayer: DplayerService ) { }

  ngOnInit(): void {

    this.dplayer.getDplayer()
    .subscribe( resp => {
      console.log(resp);
    } )

  }

}
