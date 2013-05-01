<?php

$hut_slides = array("hutSlides/slide1.png",
			"hutSlides/slide2.png",
			"hutSlides/slide3.png",
			"hutSlides/slide4.png",
			"hutSlides/slide5.png",
			"hutSlides/slide6.png");
$slide_times = array(1,
				2,
				5,
				-1,
				7,
				1);
				
$slides=array("slides"=>$hut_slides,
		"times"=>$slide_times);

$Json_slides = json_encode($slides);

echo($Json_slides);
?>
