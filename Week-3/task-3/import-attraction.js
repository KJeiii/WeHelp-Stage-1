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

    // dynamicaly create computer-mode div
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
};

GetAttraction();




