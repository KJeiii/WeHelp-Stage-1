const url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";

const GetAttraction = async() => {

    // connect to url and extract results
    const response = await fetch(url);
    const data = await response.json();
    const result = await data["result"]["results"];
    
    // create an array
    // contain pic url and attraction name
    const picAndAttraction = [];
    result.forEach(element => {
        const stitlePic = [];

       // find attraction name (stitle property) and push in stitlePic array
        let stitle = element["stitle"];
        stitlePic.push(stitle);
        
        // find first url of pic and push in stitlePic array
        let//
        file = element["file"],
        picUrl = file.split("https://"),
        firstPicUrl = picUrl[1];
        
        stitlePic.push(firstPicUrl);
        picAndAttraction.push(stitlePic);
    });   

    // ----- create computer-mode div -----
    // gallery-top
    let galleryTopDiv = document.querySelector(".gallery-top");
    for ( let i = 0 ; i < 3;  i++) {
        let galleryTopElementDiv = document.createElement("div");
        galleryTopElementDiv.setAttribute("class", "gallery-top-element");

        let topImgDiv = document.createElement("div");
        topImgDiv.setAttribute("class", "top-img-div");

        let img = document.createElement("img");
        img.setAttribute("class", "top-img");
        img.setAttribute("src", "https://" + picAndAttraction[i][1]);

        let textTopDiv = document.createElement("div");
        textTopDiv.setAttribute("class", "text-top");
        textTopDiv.textContent = picAndAttraction[i][0];

        topImgDiv.appendChild(img);
        galleryTopElementDiv.appendChild(topImgDiv);
        galleryTopElementDiv.appendChild(textTopDiv);

        galleryTopDiv.appendChild(galleryTopElementDiv);        
    }

    // gallery-center
    let galleryCenterDiv = document.querySelector(".gallery-center");
    for ( let i = 3; i < 9; i++ ) {
        let galleryCenterElementDiv = document.createElement("div");
        galleryCenterElementDiv.setAttribute("class", "gallery-center-element");

        let centerImgDiv = document.createElement("div");
        centerImgDiv.setAttribute("class", "center-img-div");

        let img = document.createElement("img");
        img.setAttribute("class", "center-img");
        img.setAttribute("src", "https://" + picAndAttraction[i][1]);


        let textCenterDiv = document.createElement("div");
        textCenterDiv.setAttribute("class", "text-center");
        textCenterDiv.textContent = picAndAttraction[i][0];

        centerImgDiv.appendChild(img);
        galleryCenterElementDiv.appendChild(centerImgDiv);
        galleryCenterElementDiv.appendChild(textCenterDiv);
        galleryCenterDiv.appendChild(galleryCenterElementDiv);

    }

    // bottom-center
    let galleryBottomDiv = document.querySelector(".gallery-bottom");
    for ( let i = 9; i < 15; i++ ) {
        let galleryCenterElementDiv = document.createElement("div");
        galleryCenterElementDiv.setAttribute("class", "gallery-center-element");

        let centerImgDiv = document.createElement("div");
        centerImgDiv.setAttribute("class", "center-img-div");

        let img = document.createElement("img");
        img.setAttribute("class", "center-img");
        img.setAttribute("src", "https://" + picAndAttraction[i][1]);


        let textCenterDiv = document.createElement("div");
        textCenterDiv.setAttribute("class", "text-center");
        textCenterDiv.textContent = picAndAttraction[i][0];

        centerImgDiv.appendChild(img);
        galleryCenterElementDiv.appendChild(centerImgDiv);
        galleryCenterElementDiv.appendChild(textCenterDiv);
        galleryBottomDiv.appendChild(galleryCenterElementDiv);

    }

    // ----- create pad & mobile mode div -----
    // gallery-top-1
    let galleryTop1Div = document.querySelector(".gallery-top-1");
    for ( let i = 0 ; i < 2;  i++) {
        let galleryTopElement1Div = document.createElement("div");
        galleryTopElement1Div.setAttribute("class", "gallery-top-element-1");

        let topImgDiv = document.createElement("div");
        topImgDiv.setAttribute("class", "top-img-div");

        let img = document.createElement("img");
        img.setAttribute("class", "top-img");
        img.setAttribute("src", "https://" + picAndAttraction[i][1]);

        let textTopDiv = document.createElement("div");
        textTopDiv.setAttribute("class", "text-top");
        textTopDiv.textContent = picAndAttraction[i][0];

        topImgDiv.appendChild(img);
        galleryTopElement1Div.appendChild(topImgDiv);
        galleryTopElement1Div.appendChild(textTopDiv);

        galleryTop1Div.appendChild(galleryTopElement1Div);        
    };
    // gallery-top-2
    let galleryTop2Div = document.querySelector(".gallery-top-2");
    for ( let i = 2 ; i < 3;  i++) {
        let galleryTopElement2Div = document.createElement("div");
        galleryTopElement2Div.setAttribute("class", "gallery-top-element-2");

        let topImgDiv = document.createElement("div");
        topImgDiv.setAttribute("class", "top-img-div");

        let img = document.createElement("img");
        img.setAttribute("class", "top-img");
        img.setAttribute("src", "https://" + picAndAttraction[i][1]);

        let textTopDiv = document.createElement("div");
        textTopDiv.setAttribute("class", "text-top");
        textTopDiv.textContent = picAndAttraction[i][0];

        topImgDiv.appendChild(img);
        galleryTopElement2Div.appendChild(topImgDiv);
        galleryTopElement2Div.appendChild(textTopDiv);

        galleryTop2Div.appendChild(galleryTopElement2Div);        
    };
    // gallery-pad-center
    let galleryPadCenterDiv = document.querySelectorAll(".gallery-pad-center");
    // first row
    for ( let i = 3 ; i < 7;  i++) {
        let galleryPadCenterElemetDiv = document.createElement("div");
        galleryPadCenterElemetDiv.setAttribute("class", "gallery-pad-center-element");

        let centerImgDiv = document.createElement("div");
        centerImgDiv.setAttribute("class", "center-img-div");

        let img = document.createElement("img");
        img.setAttribute("class", "center-img");
        img.setAttribute("src", "https://" + picAndAttraction[i][1]);

        let textCenterDiv = document.createElement("div");
        textCenterDiv.setAttribute("class", "text-center");
        textCenterDiv.textContent = picAndAttraction[i][0];

        centerImgDiv.appendChild(img);
        galleryPadCenterElemetDiv.appendChild(centerImgDiv);
        galleryPadCenterElemetDiv.appendChild(textCenterDiv);

        galleryPadCenterDiv[0].appendChild(galleryPadCenterElemetDiv);        
    };
    // second row
    for ( let i = 7 ; i < 11;  i++) {
        let galleryPadCenterElemetDiv = document.createElement("div");
        galleryPadCenterElemetDiv.setAttribute("class", "gallery-pad-center-element");

        let centerImgDiv = document.createElement("div");
        centerImgDiv.setAttribute("class", "center-img-div");

        let img = document.createElement("img");
        img.setAttribute("class", "center-img");
        img.setAttribute("src", "https://" + picAndAttraction[i][1]);

        let textCenterDiv = document.createElement("div");
        textCenterDiv.setAttribute("class", "text-center");
        textCenterDiv.textContent = picAndAttraction[i][0];

        centerImgDiv.appendChild(img);
        galleryPadCenterElemetDiv.appendChild(centerImgDiv);
        galleryPadCenterElemetDiv.appendChild(textCenterDiv);

        galleryPadCenterDiv[1].appendChild(galleryPadCenterElemetDiv);        
    };
    // third row
    for ( let i = 11 ; i < 15;  i++) {
        let galleryPadCenterElemetDiv = document.createElement("div");
        galleryPadCenterElemetDiv.setAttribute("class", "gallery-pad-center-element");

        let centerImgDiv = document.createElement("div");
        centerImgDiv.setAttribute("class", "center-img-div");

        let img = document.createElement("img");
        img.setAttribute("class", "center-img");
        img.setAttribute("src", "https://" + picAndAttraction[i][1]);

        let textCenterDiv = document.createElement("div");
        textCenterDiv.setAttribute("class", "text-center");
        textCenterDiv.textContent = picAndAttraction[i][0];

        centerImgDiv.appendChild(img);
        galleryPadCenterElemetDiv.appendChild(centerImgDiv);
        galleryPadCenterElemetDiv.appendChild(textCenterDiv);

        galleryPadCenterDiv[2].appendChild(galleryPadCenterElemetDiv);        
    };
};

GetAttraction();

let// 
remainingElement = 43,
elementStartToAdd = 15;

const LoadMore = async() => {
    let//
    response = await fetch(url),
    data = await response.json(),
    result = await data.result.results;
    // create an array
    // contain pic url and attraction name
    const picAndAttraction = [];
    result.forEach(element => {
        const stitlePic = [];
    // find attraction name (stitle property) and push in stitlePic array
        let stitle = element["stitle"];
        stitlePic.push(stitle);
        
        // find first url of pic and push in stitlePic array
        let//
        file = element["file"],
        picUrl = file.split("https://"),
        firstPicUrl = picUrl[1];
        
        stitlePic.push(firstPicUrl);
        picAndAttraction.push(stitlePic);
    });  
    // ----- create computer-mode div -----
    // load more elements under the bottom of bottom-center div

    // ----- create pad & mobile mode div -----
    // load more elements under the bottom of third row


    let computerModeDiv = document.querySelector(".computer-mode");
    let padModeDiv = document.querySelector(".pad-mode");

    if ( remainingElement >= 12 ) {
        // computer-mode : under gallery-bottom
        let galleryBottomDiv1 = document.createElement("div");
        galleryBottomDiv1.setAttribute("class", "gallery-bottom");
        for ( let i = elementStartToAdd; i < elementStartToAdd + 6; i++ ) {
            let galleryCenterElementDiv = document.createElement("div");
            galleryCenterElementDiv.setAttribute("class", "gallery-center-element");
            let centerImgDiv = document.createElement("div");
            centerImgDiv.setAttribute("class", "center-img-div");
            let img = document.createElement("img");
            img.setAttribute("class", "center-img");
            img.setAttribute("src", "https://" + picAndAttraction[i][1]);
            let textCenterDiv = document.createElement("div");
            textCenterDiv.setAttribute("class", "text-center");
            textCenterDiv.textContent = picAndAttraction[i][0];
            centerImgDiv.appendChild(img);
            galleryCenterElementDiv.appendChild(centerImgDiv);
            galleryCenterElementDiv.appendChild(textCenterDiv);
            galleryBottomDiv1.appendChild(galleryCenterElementDiv);
        };
        let galleryBottomDiv2 = document.createElement("div");
        galleryBottomDiv2.setAttribute("class", "gallery-bottom");
        for ( let i = elementStartToAdd + 6; i < elementStartToAdd + 12; i++ ) {
            let galleryCenterElementDiv = document.createElement("div");
            galleryCenterElementDiv.setAttribute("class", "gallery-center-element");
            let centerImgDiv = document.createElement("div");
            centerImgDiv.setAttribute("class", "center-img-div");
            let img = document.createElement("img");
            img.setAttribute("class", "center-img");
            img.setAttribute("src", "https://" + picAndAttraction[i][1]);
            let textCenterDiv = document.createElement("div");
            textCenterDiv.setAttribute("class", "text-center");
            textCenterDiv.textContent = picAndAttraction[i][0];
            centerImgDiv.appendChild(img);
            galleryCenterElementDiv.appendChild(centerImgDiv);
            galleryCenterElementDiv.appendChild(textCenterDiv);
            galleryBottomDiv2.appendChild(galleryCenterElementDiv);
        };
        computerModeDiv.append(galleryBottomDiv1, galleryBottomDiv2);

        // pad & mobile-mode : under third row
        let galleryPadCenterDiv1 = document.createElement("div");
        galleryPadCenterDiv1.setAttribute("class", "gallery-pad-center");
        for ( let i = elementStartToAdd ; i < elementStartToAdd + 4;  i++) {
            let galleryPadCenterElemetDiv = document.createElement("div");
            galleryPadCenterElemetDiv.setAttribute("class", "gallery-pad-center-element");
            let centerImgDiv = document.createElement("div");
            centerImgDiv.setAttribute("class", "center-img-div");
            let img = document.createElement("img");
            img.setAttribute("class", "center-img");
            img.setAttribute("src", "https://" + picAndAttraction[i][1]);
            let textCenterDiv = document.createElement("div");
            textCenterDiv.setAttribute("class", "text-center");
            textCenterDiv.textContent = picAndAttraction[i][0];
            centerImgDiv.appendChild(img);
            galleryPadCenterElemetDiv.appendChild(centerImgDiv);
            galleryPadCenterElemetDiv.appendChild(textCenterDiv);
            galleryPadCenterDiv1.appendChild(galleryPadCenterElemetDiv);        
        };
        let galleryPadCenterDiv2 = document.createElement("div");
        galleryPadCenterDiv2.setAttribute("class", "gallery-pad-center");
        for ( let i = elementStartToAdd + 4 ; i < elementStartToAdd + 8;  i++) {
            let galleryPadCenterElemetDiv = document.createElement("div");
            galleryPadCenterElemetDiv.setAttribute("class", "gallery-pad-center-element");
            let centerImgDiv = document.createElement("div");
            centerImgDiv.setAttribute("class", "center-img-div");
            let img = document.createElement("img");
            img.setAttribute("class", "center-img");
            img.setAttribute("src", "https://" + picAndAttraction[i][1]);
            let textCenterDiv = document.createElement("div");
            textCenterDiv.setAttribute("class", "text-center");
            textCenterDiv.textContent = picAndAttraction[i][0];
            centerImgDiv.appendChild(img);
            galleryPadCenterElemetDiv.appendChild(centerImgDiv);
            galleryPadCenterElemetDiv.appendChild(textCenterDiv);
            galleryPadCenterDiv2.appendChild(galleryPadCenterElemetDiv);        
        };
        let galleryPadCenterDiv3 = document.createElement("div");
        galleryPadCenterDiv3.setAttribute("class", "gallery-pad-center");

        for ( let i = elementStartToAdd + 8 ; i < elementStartToAdd + 12;  i++) {
            let galleryPadCenterElemetDiv = document.createElement("div");
            galleryPadCenterElemetDiv.setAttribute("class", "gallery-pad-center-element");
            let centerImgDiv = document.createElement("div");
            centerImgDiv.setAttribute("class", "center-img-div");
            let img = document.createElement("img");
            img.setAttribute("class", "center-img");
            img.setAttribute("src", "https://" + picAndAttraction[i][1]);
            let textCenterDiv = document.createElement("div");
            textCenterDiv.setAttribute("class", "text-center");
            textCenterDiv.textContent = picAndAttraction[i][0];
            centerImgDiv.appendChild(img);
            galleryPadCenterElemetDiv.appendChild(centerImgDiv);
            galleryPadCenterElemetDiv.appendChild(textCenterDiv);
            galleryPadCenterDiv3.appendChild(galleryPadCenterElemetDiv);        
        };
        padModeDiv.append(galleryPadCenterDiv1, galleryPadCenterDiv2, galleryPadCenterDiv3);
        // add 12 to elementStartToAdd for next Loadmore()
        remainingElement -= 12;
        elementStartToAdd += 12;
    }else if ( remainingElement < 12 && remainingElement > 0 ){
        // computer-mode:
        // create flex-wrap div
        let galleryLoadMoreDiv = document.createElement("div");
        galleryLoadMoreDiv.setAttribute("class", "gallery-load-more");
        for ( let i = elementStartToAdd; i < elementStartToAdd + remainingElement; i++ ) {
            let galleryLoadMoreElementDiv = document.createElement("div");
            galleryLoadMoreElementDiv.setAttribute("class", "gallery-load-more-element");
            let centerImgDiv = document.createElement("div");
            centerImgDiv.setAttribute("class", "center-img-div");
            let img = document.createElement("img");
            img.setAttribute("class", "center-img");
            img.setAttribute("src", "https://" + picAndAttraction[i][1]);
            let textCenterDiv = document.createElement("div");
            textCenterDiv.setAttribute("class", "text-center");
            textCenterDiv.textContent = picAndAttraction[i][0];
            centerImgDiv.appendChild(img);
            galleryLoadMoreElementDiv.appendChild(centerImgDiv);
            galleryLoadMoreElementDiv.appendChild(textCenterDiv);
            galleryLoadMoreDiv.appendChild(galleryLoadMoreElementDiv);
        };
        computerModeDiv.appendChild(galleryLoadMoreDiv)

        // computer-mode:
        // create flex-wrap div 
        let galleryPadLoadMoreDiv = document.createElement("div");
        galleryPadLoadMoreDiv.setAttribute("class", "gallery-pad-load-more");

        for ( let i = elementStartToAdd ; i < elementStartToAdd + remainingElement;  i++) {
            let galleryPadLoadMoreElemetDiv = document.createElement("div");
            galleryPadLoadMoreElemetDiv.setAttribute("class", "gallery-pad-load-more-element");
            let centerImgDiv = document.createElement("div");
            centerImgDiv.setAttribute("class", "center-img-div");
            let img = document.createElement("img");
            img.setAttribute("class", "center-img");
            img.setAttribute("src", "https://" + picAndAttraction[i][1]);
            let textCenterDiv = document.createElement("div");
            textCenterDiv.setAttribute("class", "text-center");
            textCenterDiv.textContent = picAndAttraction[i][0];
            centerImgDiv.appendChild(img);
            galleryPadLoadMoreElemetDiv.appendChild(centerImgDiv);
            galleryPadLoadMoreElemetDiv.appendChild(textCenterDiv);
            galleryPadLoadMoreDiv.appendChild(galleryPadLoadMoreElemetDiv);        
        };
        padModeDiv.appendChild(galleryPadLoadMoreDiv);


        remainingElement -= 12;
        elementStartToAdd += 12;

    }else{
        let btn = document.querySelector(".btn");
        btn.innerHTML = "No More~";
    };
};




