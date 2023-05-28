<template>
	<div>
    <br>
    <div class="container">
    <div class="box">
        <h3 style="margin-top: 10px;">Predict Movie Revenue of Actors</h3>
    </div>
    </div>
    <br>
    <img src = "@/assets/money.png" class="img-fluid" />
    <br>
    <input ref="cursorpredict" type="text" v-model="actor_search" @keyup.enter="actorSearch()" value="search">
    &nbsp;
    <button type="button" class="btn btn-outline-secondary" @click="actorSearch()">actor_search</button>
    <br><br>
    <ul>
    <h5>Picked Actors</h5>
    </ul>
    <span v-for="pick_actor in pick_actors" :key="pick_actor.id.id">
        
        <button type="button" class="btn btn-outline-secondary">
                {{pick_actor.name}}
        </button>
    </span>
    <br>
    <ul v-if="result">
    <p> 결과 : {{ result }} (원) </p>
    <button type="button" class="btn btn-outline-primary" style="" @click="reset_result"> 
    reset
    </button>
    </ul>
    <br>
    <ul>
    <button type="button" class="btn btn-outline-secondary" @click="movieRevenue">확인</button>
    </ul>
    <!-- <button @click="resetActor">초기화</button> -->

    <br>
    <br>
    <hr style="margin: auto; width: 60%;">
    <br>
    <!-- <div class="row row-cols-1 row-cols-md-2 g-4">
        <div class="col">
            <div class="card">
                <img src="..." class="card-img-top" alt="">
                    <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            </div>
        </div>
    </div>
    </div> -->
    <ul v-if="check" class="scroll-container">
    <button type="button" class="btn btn-outline-secondary" style="margin-bottom: 10px;" @click="ale">배우</button>
    <br><br>
    <!-- <div data-bs-spy="scroll";> -->
    <div id="new_container" class="row row-cols-1 row-cols-md-6 g-4">
    <!-- <div class="hstack gap-3"> -->
        <div v-for="actor in AllActors" :key="actor.id" :actor="actor" style="margin-bottom: 20px;">
            <div class="col">
            <div class="card" style="width: 200px;">
            <div class="card-custom">
            <img class="p-2" :src="`https://image.tmdb.org/t/p/w138_and_h175_face/${actor.profile_path}`" style="border-radius: 20%;">
            <div class="card-body" style="margin: 0px; padding: 0px;">
            <span class="card-title">
            <button type="button" class="btn btn-outline-dark" style="margin-top: 10px; margin-bottom: 20px; color: black;" @click="pickActor(actor)">{{ actor.name }}</button>
            </span>
        </div>
        </div>
    <!-- </div> -->
    </div>
    </div>
    </div>
    </div>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'PredictMovieView',
  data() {
    return {
      pick_actor: null,
      pick_actors:[],
      pick_actors_name: [],
      AllActors: [],
      Actors: [],
      result: null,
      actor_search: null,
      acto: null,
      check: false,
    }
  },
  // created(){
  //   this.getAllActors()
  // },
  // mounted() {
  //   this.startCursor()
  // },
  methods: {
    reset_result() {
        return this.result = 0
    },
    ale(){
        return alert('배우를 골라라')
    },
    // getAllActors() {
		// 	axios({
		// 		method:'get',
    //     url:'https://api.themoviedb.org/3/person/popular?language=ko-KR&page=1&api_key=c988dcefc9872e7d8eb4a1b1592fd0c8',
		// 	})
		// 	.then((res) => {
		// 		// console.log(res.data.results)
		// 		this.AllActors = res.data.results
    //   })
    //   .catch((err) => {
    //   console.log(err)
    //   })
		// },
    // resetActor () {
    //   this.pick_actors = null
    //   // location.reload(true)
    // },
    pickActor(id) {
      const pick_actors = this.pick_actors
      // console.log(pick_actors)
      const pick_actor = id
      // console.log(pick_actor)
      // console.log(this.pick_actors)
      if(pick_actors.includes(pick_actor)){
        // alert('이미 선택된 배우입니다')
        const filter_actors = pick_actors.filter((element) => element !== pick_actor)
        this.pick_actors = filter_actors
        // console.log(this.pick_actors)
        // this.pick_actor = null
      } else if (this.pick_actors.length >= 4){
        alert('4명까지만 선택해주세요')
      } else {
        pick_actors.push(pick_actor)
        this.pick_actors=pick_actors
        // console.log(this.pick_actors)
      }

    },
  
    movieRevenue(){
      const pick_actors = this.pick_actors
      const pick_actors_name = this.pick_actors_name
      // console.log(pick_actors)
      for (const pick_actor of pick_actors){
        console.log(pick_actor)
        pick_actors_name.push(pick_actor.name)
      }
      const actors = pick_actors_name
      this.pick_actors = []
      this.pick_actors_name = []
      console.log(actors);
      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/movies/predicts/`,
        data: {
          actors
        }
      })
      .then((res) => {
        // console.log(res)
        // console.log(actors)
        this.pick_actors == null
        this.result = res.data
      })
      .catch((err) => {
        console.log(err)
        this.pick_actors == null
      })

    },
    actorSearch() {
        this.check = true
      this.AllActors = []
      const query = this.actor_search
      // console.log(query)
      axios({
        method: 'GET',
        url: `https://api.themoviedb.org/3/search/person?include_adult=false&language=en-US&page=1&api_key=c988dcefc9872e7d8eb4a1b1592fd0c8&query=${query}`,
        //url 1페이지만 갖고 오도록 해놓음
      })
      .then((res) => {
        // console.log(res.data.results)
        const actos = res.data.results
        const AllActors = this.AllActors
        actos.forEach(element => {
          if (element.popularity>4 ) {
            if (element.known_for_department == "Acting"){
              if(element.profile_path != null){
                // console.log(element)
                AllActors.push(element)
                // console.log(AllActors)
              }
            }
          }
        })
        // console.log(AllActors) 
        this.actor_search = null
        this.Cursorpredict()
        // console.log(AllActors)
      })
      .catch((err) => console.log(err))
    },
    
    Cursorpredict() {
      this.$refs.cursorpredict.focus()
    },
  }
}

</script>

<style>
.container {
  display: flex;
  align-items: center;
  justify-content: center;
  /* height: 100vh; */
}

.box {
  font-weight: bold;
  background-color: black;
  color: white;
  height: 50px;
  width: 60%;
}
.scroll_container {
  width: 100%;
  overflow-x: scroll;
  white-space: nowrap;
}

#new_container {
  height: 500px;
  overflow: auto;
}
::-webkit-scrollbar {
  width: 10px;
  height: 20px;
}
::-webkit-scrollbar-thumb {
  /* background: 스크롤바 막대 색상 black; */
  border-radius: 10%;
}
.card-custom {
  /* 원하는 카드 크기로 조정 */
  width: 200px;
  height: 250px;
  margin: 0px;
  background-color: rgb(241, 240, 240);
}
</style>