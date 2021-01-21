import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home/home.component';
import { ProfileComponent } from './profile/profile.component';
import { ListRankComponent } from './list-rank/list-rank.component';
import { ComponentsModule } from '../components/components.module';



@NgModule({
  declarations: [HomeComponent, ProfileComponent, ListRankComponent],
  imports: [
    CommonModule,
    ComponentsModule
  ]
})
export class PagesModule { }
