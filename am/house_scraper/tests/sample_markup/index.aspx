

<!DOCTYPE html public"-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" >
<head><link rel="stylesheet" type="text/css" href="/DXR.axd?r=1_32-Xkrgd" /><link rel="stylesheet" type="text/css" href="sidebar.css" /><meta http-equiv="X-UA-Compatible" content="IE=Edge" /><link href="./StyleSheet.css" type="text/css" rel="stylesheet" /><title>
	Missouri House of Representatives
</title>
    <script language="javascript" type="text/javascript">
    
    var overpopout = 0;
    
    function Popout(targetid)
    {
        if (document.getElementById(targetid) != null) {
         document.getElementById(targetid).style.display="block";
      } 
    }
    
    function CollapsePopout(targetid)
    {
        if (document.getElementById(targetid) != null) {
         document.getElementById(targetid).style.display="none";
         overpopout = 0;
      } 
    }
    
    function OntoPopout()
    {
        overpopout = 1; 
    }
      
    function LeaveMenuBar(targetid)
    {
        if (overpopout == 0 && document.getElementById(targetid) != null)
        {        
            CollapsePopout(targetid);
       }
    }
    </script>
    <style>
        .header 
        {
            background:#C0C0C0 url('graphics/header0.jpg');
        }
    </style>
    
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
<script type="text/javascript" src="scripts/jquery.maskedinput-1.3.min.js"></script>
<script src="./Scripts/newsroller.js" type="text/javascript"></script>
<link href="./newsroller.css" type="text/css" rel="stylesheet" />
<style type="text/css">
#hearingbox 
{
    background-color:rgba(255, 255, 255, 0.5);
    border:1px solid gray;
    height:70px;
    width:390px;
    overflow:hidden;
}
.budgetometer
{
    text-align:center;
    width:100%;
    height:32px;
    vertical-align:top;
    margin:3px;
}
.budgetsection 
{
    display:inline-block;
    width:53px;
    height:34px;
    vertical-align:middle;
    line-height:17px;
    border:1px solid black;
    font-size:10pt;
    white-space:nowrap;
    overflow:hidden;
    text-overflow: ellipsis;
    color:transparent;
}
.budgetsection a
{
    outline:none;
    display:inline-block;
    vertical-align:middle;
    line-height:normal;
    padding-left:2px;
    padding-right:2px;
}
.budgetsection a:hover
{
    text-decoration:none;
}
.budgetcomplete 
{
    background-color: #19E6B8;
    background-image: url('graphics/budgetcomplete.png');
}
.budgetinprogress
{
    background-color: #FFD200;
    background-image: url('graphics/budgetinprogress.png');
}
.budgetincomplete
{
    background-color: #D1D1D1;
    background-image: url('graphics/budgetincomplete.png');
}
.bo1 
{
    border-radius: 40px 0px 0px 40px;
}
.bo2 
{
    border-radius: 0px 40px 40px 0px;
}
.budgetometerexplanation
{
    display:block; 
    height:0px;
    position:absolute;
    width:499px;
    margin-right:auto;
    margin-left:auto;
    top:279px;
    display:none;
}
.downshiftexp
{
    margin-top:51px !important;
}
.budgetometerexplanation span
{
    border:1px solid gray;
    display:inline-block;
    padding:3px;
    width:480px;
    background-color:rgba(255, 255, 255, 0.9);
    margin-top:15px;
    margin-right:auto;
    margin-left:auto;
    border-radius:8px;
    text-indent:-20px;
}

.budgetometerexplanationcurrent span
{
    border:1px solid gray;
    display:inline-block;
    padding:3px;
    width:384px;
    background-color:rgba(255, 255, 255, 0.9);
    word-wrap: break;
    border-radius:4px;  
    
    font-size: 10pt;  
}
</style>
<script type="text/javascript">
    function launch() {
        window.open('housefrm.html', "house", "height=222, width=350, resizable=1, menubar=0, location=0", 0);
    }
    function ReplaceImage(img_name, img_src)
    { document[img_name].src = img_src; }

    jQuery(function ($) {
        $("#zipcode").mask("99999-?9999");
    });

    function galleryswitch() {
        document.getElementById('gallerybox').style.display = "none";
        document.getElementById('famousbox').style.display = "inline";
    }
    function famousswitch() {
        document.getElementById('famousbox').style.display = "none";
        document.getElementById('gallerybox').style.display = "inline";
    }
    var live = 0;
    function DisplayLiveAudio() {
        if (live == 0) {
            document.getElementById('LiveAudio').style.display = "block";
            live = 1;
        }
        else {
            document.getElementById('LiveAudio').style.display = "none";
            live = 0;
        }
    }
    function PopoutAudio() {
		window.open("AudioPopout.html", "audiopopout", "toolbar=no, scrollbars=no, resizable=yes, top=500, left=500, width=408, height=521");
		return false;
	}
    
    function PopoutAlt() {
        window.open("http://chamber.house.mo.gov/housechamber", "videopopout", "toolbar=no, scrollbars=no, resizable=yes, top=500, left=500, width=300, height=60");
        return false;
    }
    
	function PopoutVideo() {
	    window.open("vidframe.aspx?publish_id=1&embed=1&player_width=720&player_height=480", "videopopout", "toolbar=no, scrollbars=no, resizable=yes, top=500, left=500, width=720, height=547");
	    return false;
	}
    function ShowBudgetSec(sec) {
        for (i = 0; i < 7; i++) {
            if (i == sec)
                document.getElementById("budgetometerexplanation" + sec).style.display = "block";
            else
                document.getElementById("budgetometerexplanation" + i).style.display = "none";
        }    
}
</script>
    <style>
.header {
background:#C0C0C0 url('graphics/header1.jpg');
}
</style>
    
</head>
<body>    
    <form method="post" action="./" id="form1">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="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" />

<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="CA0B0334" />
<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEdAAf0CeiyXvd65bZ2aM9LpIa84+3WpZQNb82rzs2KnT3rh1V6RkAfufrqJa6LpqnGFgv71KuMUeAEIQs6+hzvmiFbn1RcjtHAj66REed34CUNnj7/hqqhBLii75HXRTaFMR6V2GgTMfP5HMfcPsccbyUvHJZ++BuOxaZYKyhjjY7voSFHUine5IOaYb/FWrQ9RGo=" />
    <div id="outer"><div id="main">
    
        <div class="header">
            <div style="padding-top:0px;float:left;">
            <a href="/"><div style="width:690px;height:175px;"></div></a>
            </div>
            <div style="padding-top:130px;float:right;">
            <div class="searchbar"><label for="txtSearch" style="display: block; color: rgb(79, 76, 76); text-shadow: 0px 1px rgb(255, 255, 255); background: rgba(245, 245, 220, 0.7); text-indent: 107px;">Bill Search</label><input name="ctl00$txtSearch" type="text" id="txtSearch" />
            <input type="submit" name="ctl00$btnSearch" value="Go" id="btnSearch" /></div>
            </div>

            <!-- a href="http://www.house.mo.gov"><img alt="Missouri House of Representatives" src="./graphics/header0.jpg" border="0" /></a -->
        </div>
        <div id="subheaderbuttons">
            <a href="/" class="subheadbutton">Home</a>
            <a href="/HearingDisplay/" class="subheadbutton">Hearings</a>
            <a href="DailyCalendar.aspx" class="subheadbutton">Calendar</a>
            <a href="JournalList.aspx" class="subheadbutton">Journal</a>
            <a href="budget.aspx" class="subheadbutton">FY2018 Budget</a>
        </div>
    <div class="mainbody">
        <div id="left">
            <div id="sidelinks">
                <div class="blockheader">
                    &nbsp;
                </div>
                <input type="hidden"/><script id="dxis_247559926" src="/DXR.axd?r=1_225-Xkrgd" type="text/javascript"></script><script id="dxis_180154157" src="/DXR.axd?r=1_130-Xkrgd" type="text/javascript"></script><script id="dxis_480463454" src="/DXR.axd?r=1_218-Xkrgd" type="text/javascript"></script><script id="dxis_899364636" src="/DXR.axd?r=1_164-Xkrgd" type="text/javascript"></script><script id="dxis_1811627227" src="/DXR.axd?r=1_127-Xkrgd" type="text/javascript"></script><script id="dxis_552757894" src="/DXR.axd?r=1_210-Xkrgd" type="text/javascript"></script><script id="dxis_1148696100" src="/DXR.axd?r=1_216-Xkrgd" type="text/javascript"></script><script id="dxis_1327249696" src="/DXR.axd?r=1_201-Xkrgd" type="text/javascript"></script><div class="dxmLite_PlasticBlue dxm-ltr">
	<div class="dxm-main dxm-vertical" id="ASPxMenu1">
		<ul class="dx dxm-image-l dxm-noImages dxm-gutter">
			<li class="dxm-item SideMenuItem dxm-subMenu"><a class="dxm-content dxm-hasText dx" href="sitemap.aspx?pid=16"><span class="dx-vam">House Members</span></a><div class="dxm-popOut">
				<img class="dxm-pImage" src="graphics/altright.png" alt=">" />
			</div><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideMenuItem dxm-subMenu"><a class="dxm-content dxm-hasText dx" href="sitemap.aspx?pid=13"><span class="dx-vam">Bill Information</span></a><div class="dxm-popOut">
				<img class="dxm-pImage" src="graphics/altright.png" alt=">" />
			</div><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideMenuItem dxm-subMenu"><a class="dxm-content dxm-hasText dx" href="sitemap.aspx?pid=18"><span class="dx-vam">Committees</span></a><div class="dxm-popOut">
				<img class="dxm-pImage" src="graphics/altright.png" alt=">" />
			</div><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideMenuItem dxm-subMenu"><a class="dxm-content dxm-hasText dx" href="sitemap.aspx?pid=136"><span class="dx-vam">Media Center</span></a><div class="dxm-popOut">
				<img class="dxm-pImage" src="graphics/altright.png" alt=">" />
			</div><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideMenuItem dxm-subMenu"><a class="dxm-content dxm-hasText dx" href="sitemap.aspx?pid=19"><span class="dx-vam">General Information</span></a><div class="dxm-popOut">
				<img class="dxm-pImage" src="graphics/altright.png" alt=">" />
			</div><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="sitemap.aspx?pid=24"><span class="dx-vam">Past Session Archives</span></a><b class="dx-clear"></b></li>
		</ul>
	</div><b class="dx-clear"></b><div id="ASPxMenu1_DXM0_" style="z-index:20000;display:none;">
		<div class="dxm-shadow dxm-popup SideSubMenu">
			<ul class="dx dxm-noImages">
				<li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./member.aspx"><span class="dx-vam">Directory of Representatives</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./houseleadership.aspx"><span class="dx-vam">House Leadership</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./legislatorlookup.aspx"><span class="dx-vam">Legislator Lookup</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="sitemap.aspx?pid=388"><span class="dx-vam">General Info</span></a><b class="dx-clear"></b></li>
			</ul>
		</div>
	</div><div id="ASPxMenu1_DXM1_" style="z-index:20000;display:none;">
		<div class="dxm-shadow dxm-popup SideSubMenu">
			<ul class="dx dxm-noImages">
				<li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./billlist.aspx"><span class="dx-vam">Bill List</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="billcentral.aspx?pid=26"><span class="dx-vam">Bill Tracking</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="sitemap.aspx?pid=32"><span class="dx-vam">Bill Activity Reports</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-subMenu"><a class="dxm-content dxm-hasText dx" href="sitemap.aspx?pid=389"><span class="dx-vam">Floor Activity</span></a><div class="dxm-popOut">
					<img class="dxm-pImage" src="graphics/altright.png" alt=">" />
				</div><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./budget.aspx"><span class="dx-vam">FY2018 Budget Process</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./content.aspx?info=/info/cpyright.htm"><span class="dx-vam">Copyright Information</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./content.aspx?info=/bills151/dates.htm"><span class="dx-vam">Dates of Interest</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="http://house.mo.gov/subjectindexlist.aspx"><span class="dx-vam">Subject Index</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="http://house.mo.gov/pr/TAFP2016.pdf"><span class="dx-vam">Bills Truly Agreed &amp; Finally Passed Summaries 2016</span></a><b class="dx-clear"></b></li>
			</ul>
		</div>
	</div><div id="ASPxMenu1_DXM1i3_" style="z-index:20002;display:none;">
		<div class="dxm-shadow dxm-popup SideSubMenu">
			<ul class="dx dxm-noImages">
				<li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./DailyCalendar.aspx"><span class="dx-vam">House Calendar</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./content.aspx?info=/info/schedule.htm"><span class="dx-vam">House Floor Schedule</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./DailyActivity.aspx"><span class="dx-vam">Current House Actions</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./dailyactivitylist.aspx"><span class="dx-vam">Past House Actions</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./DailyRollCallList.aspx"><span class="dx-vam">Daily Roll Calls</span></a><b class="dx-clear"></b></li>
			</ul>
		</div>
	</div><div id="ASPxMenu1_DXM2_" style="z-index:20000;display:none;">
		<div class="dxm-shadow dxm-popup SideSubMenu">
			<ul class="dx dxm-noImages">
				<li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./CommitteeList.aspx"><span class="dx-vam">Committee Assignments</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./ActiveCommittees.aspx"><span class="dx-vam">House Committees</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./SelectCommitteeHierarchy.aspx"><span class="dx-vam">Committee Organization</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./CommDescript.aspx"><span class="dx-vam">Committee Descriptions</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-subMenu"><a class="dxm-content dxm-hasText dx" href="sitemap.aspx?pid=15"><span class="dx-vam">Hearing Schedules</span></a><div class="dxm-popOut">
					<img class="dxm-pImage" src="graphics/altright.png" alt=">" />
				</div><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./CommitteeSchedule.aspx"><span class="dx-vam">Hearing Room Schedule</span></a><b class="dx-clear"></b></li>
			</ul>
		</div>
	</div><div id="ASPxMenu1_DXM2i4_" style="z-index:20002;display:none;">
		<div class="dxm-shadow dxm-popup SideSubMenu">
			<ul class="dx dxm-noImages">
				<li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./HearingsDateOrder.aspx"><span class="dx-vam">House Hearing Schedule</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="http://www.senate.mo.gov/hearingsschedule/hrings.htm"><span class="dx-vam">Senate Hearing Schedule</span></a><b class="dx-clear"></b></li>
			</ul>
		</div>
	</div><div id="ASPxMenu1_DXM3_" style="z-index:20000;display:none;">
		<div class="dxm-shadow dxm-popup SideSubMenu">
			<ul class="dx dxm-noImages">
				<li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./news.aspx?"><span class="dx-vam">Latest News</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./content.aspx?info=/video.htm"><span class="dx-vam">Video</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./content.aspx?info=/photos.htm"><span class="dx-vam">Photos</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./content.aspx?info=/staff.htm"><span class="dx-vam">Media Staff</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-subMenu"><a class="dxm-content dxm-hasText dx" href="./content.aspx?info=/link2/debates.txt"><span class="dx-vam">Live Debates</span></a><div class="dxm-popOut">
					<img class="dxm-pImage" src="graphics/altright.png" alt=">" />
				</div><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="http://house.mo.gov/AudioArchive.aspx"><span class="dx-vam">Debate Archive</span></a><b class="dx-clear"></b></li>
			</ul>
		</div>
	</div><div id="ASPxMenu1_DXM3i4_" style="z-index:20002;display:none;">
		<div class="dxm-shadow dxm-popup SideSubMenu">
			<ul class="dx dxm-noImages">
				<li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="http://house.mo.gov/AudioPopout.html"><span class="dx-vam">House Debate</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="mms://chamber.senate.mo.gov/SenateChamber"><span class="dx-vam">Senate Debate</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./content.aspx?info=/link2/debates.txt"><span class="dx-vam">Problems with Audio</span></a><b class="dx-clear"></b></li>
			</ul>
		</div>
	</div><div id="ASPxMenu1_DXM4_" style="z-index:20000;display:none;">
		<div class="dxm-shadow dxm-popup SideSubMenu">
			<ul class="dx dxm-noImages">
				<li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./chiefclerk.aspx"><span class="dx-vam">Chief Clerk of the House</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./journallist.aspx"><span class="dx-vam">Journal of the House</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./content.aspx?info=/bills151/dates.htm"><span class="dx-vam">Dates of Interest</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./billtracking/bills171/rules/rules.pdf"><span class="dx-vam">Rules of the House (PDF)</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="http://www.moga.mo.gov/htmlpages2/statuteconstitutionsearch.aspx"><span class="dx-vam">Missouri Constitution</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="http://www.moga.mo.gov/mostatutes/statutesAna.html"><span class="dx-vam">Missouri Statutes</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-subMenu"><a class="dxm-content dxm-hasText dx" href="sitemap.aspx?pid=103"><span class="dx-vam">The Legislative Process</span></a><div class="dxm-popOut">
					<img class="dxm-pImage" src="graphics/altright.png" alt=">" />
				</div><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-subMenu"><a class="dxm-content dxm-hasText dx" href="sitemap.aspx?pid=22"><span class="dx-vam">House Information</span></a><div class="dxm-popOut">
					<img class="dxm-pImage" src="graphics/altright.png" alt=">" />
				</div><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem dxm-noSubMenu"><a class="dxm-content dxm-hasText dx" href="./billtracking/info/knowMOspread.pdf"><span class="dx-vam">Do You Know MO? Handbook (PDF)</span></a><b class="dx-clear"></b></li>
			</ul>
		</div>
	</div><div id="ASPxMenu1_DXM4i6_" style="z-index:20002;display:none;">
		<div class="dxm-shadow dxm-popup SideSubMenu">
			<ul class="dx dxm-noImages">
				<li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./content.aspx?info=/info/howbill.htm"><span class="dx-vam">Making The Law</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./billtracking/info/habbl.pdf"><span class="dx-vam">How a Bill Becomes Law (PDF)</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./content.aspx?info=/info/glossary.htm"><span class="dx-vam">Glossary of Terms</span></a><b class="dx-clear"></b></li>
			</ul>
		</div>
	</div><div id="ASPxMenu1_DXM4i7_" style="z-index:20002;display:none;">
		<div class="dxm-shadow dxm-popup SideSubMenu">
			<ul class="dx dxm-noImages">
				<li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./jobpostings.aspx"><span class="dx-vam">Employment Opportunities</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./docs/?s=intern"><span class="dx-vam">Intern Activities</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./bidposting.aspx"><span class="dx-vam">Current Bid Items</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./rotundaschedule.aspx"><span class="dx-vam">Third Floor Rotunda Schedule</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./content.aspx?info=/info/capitolfloors.htm"><span class="dx-vam">Capitol Floor Maps</span></a><b class="dx-clear"></b></li><li class="dxm-spacing"></li><li class="dxm-item SideSubMenuItem"><a class="dxm-content dxm-hasText dx" href="./content.aspx?info=/info/CAPTOUR.HTM"><span class="dx-vam">Visiting The House</span></a><b class="dx-clear"></b></li>
			</ul>
		</div>
	</div>
</div><script id="dxss_2112659133" type="text/javascript">
<!--
ASPx.AddHoverItems('ASPxMenu1',[[['dxm-hovered','',''],['','',''],['DXI0_','DXI1_','DXI1i0_','DXI1i1_','DXI1i2_','DXI1i3_','DXI1i4_','DXI1i5_','DXI1i6_','DXI1i7_','DXI1i8_','DXI2_','DXI2i0_','DXI2i1_','DXI2i2_','DXI2i3_','DXI2i4_','DXI2i5_','DXI3_','DXI3i0_','DXI3i1_','DXI3i2_','DXI3i3_','DXI3i4_','DXI3i5_','DXI4_','DXI4i0_','DXI4i1_','DXI4i2_','DXI4i3_','DXI4i4_','DXI4i5_','DXI4i6_','DXI4i7_','DXI4i8_','DXI5_'],['','P','T']],[[''],[''],['DXME0_','DXMBC0_','DXME1_','DXMBC1_','DXME1i3_','DXMBC1i3_','DXME2_','DXMBC2_','DXME2i4_','DXMBC2i4_','DXME3_','DXMBC3_','DXME3i4_','DXMBC3i4_','DXME4_','DXMBC4_','DXME4i6_','DXMBC4i6_','DXME4i7_','DXMBC4i7_']],[['dxm-hovered',''],['',''],['DXI0i0_','DXI0i1_','DXI0i2_','DXI0i3_','DXI1i3i0_','DXI1i3i1_','DXI1i3i2_','DXI1i3i3_','DXI1i3i4_','DXI2i4i0_','DXI2i4i1_','DXI3i4i0_','DXI3i4i1_','DXI3i4i2_','DXI4i6i0_','DXI4i6i1_','DXI4i6i2_','DXI4i7i0_','DXI4i7i1_','DXI4i7i2_','DXI4i7i3_','DXI4i7i4_','DXI4i7i5_'],['','T']]]);

var dxo = new ASPxClientMenu('ASPxMenu1');
window['ASPxMenu1'] = dxo;
dxo.uniqueID = 'ctl00$ASPxMenu1';
dxo.renderData={'':[[0],[1],[2],[3],[4],[5]],'0':[[0],[1],[2],[3]],'1':[[0],[1],[2],[3],[4],[5],[6],[7],[8]],'1i3':[[0],[1],[2],[3],[4]],'2':[[0],[1],[2],[3],[4],[5]],'2i4':[[0],[1]],'3':[[0],[1],[2],[3],[4],[5]],'3i4':[[0],[1],[2]],'4':[[0],[1],[2],[3],[4],[5],[6],[7],[8]],'4i6':[[0],[1],[2]],'4i7':[[0],[1],[2],[3],[4],[5]]};
dxo.subMenuFIYOffset=-1;
dxo.subMenuLIYOffset=-1;
dxo.subMenuYOffset=-1;
dxo.rootSubMenuFIYOffset=-1;
dxo.rootSubMenuLIYOffset=-1;
dxo.rootSubMenuYOffset=-1;
dxo.isVertical=true;
dxo.AfterCreate();

//-->
</script>
                <span id="lblLinks"></span>
                <div class="relatedlinks">
                    Related Links
<a href="http://house.mo.gov/content.aspx?info=/info/MU_REVIEW_COMMISSION_2016.htm">University of Missouri Review Commission</a>
<a href="http://www.mo.gov">Missouri State Government</a>
<a href="http://www.senate.mo.gov">Missouri Senate</a>
<a href="http://www.moga.mo.gov/htmlpages2/statuteconstitutionsearch.aspx">Revised Statutes of Missouri Search</a>
<a href="http://www.moga.mo.gov/mostatutes/statutesAna.html">Revised Statutes of Missouri (RSMO)</a>
<a href="http://www.moga.mo.gov/mostatutes/moconstn.html">Missouri Constitution</a>
<a href="http://capitol.mo.gov/">Capitol Commission</a>
<a href="/content.aspx?info=/info/captour.htm">Visiting the House</a>
<a href="/jobpostings.aspx">House Job Opportunities</a>
<a style="background-color:rgba(64,64,64,0.25);" href="/bidposting.aspx">Current Bid Items</a>
<a href="/content.aspx?info=/info/question.htm">Frequently Requested Resources</a>
                </div>
                <div id="legislatorlookupblock" class="block">
                    <div id="pnlSideLegLookup">
	
                    <div class="blocktitle">
                    Who is your Representative?
                    </div>
            
                    <div class="blockcontent">
        <input name="ctl00$txtzip5" type="text" maxlength="10" id="txtzip5" size="9" /> <input type="submit" name="ctl00$Button1" value="Go" id="Button1" /><br />
        <span id="Label7"><font face="Arial" size="1">(zip code or zip+4)</font></span>
                    </div>
                    <div class="blockfooter">
                        &nbsp;
                    </div>
                    
</div>
                </div>
            </div>
        </div>
    
        <div id="right">
            
     
	<div class="left">
        
        
        <div id="ContentPlaceHolder1_speakerbox" class="speakerbox generalsec" style="width:397px;height:200px;font-size:10pt">
            <div style="float:left;margin:5px;display:none;"><img src="graphics/speaker.jpg" alt="Speaker Richardson" border="0" style="border:0px solid transparent;border-radius:5px;" /></div>
			<div id="welcome" style="padding:10px;font-size:11pt;"><span style="font-weight:bold;font-size:21pt;">Welcome</span>
			to the Missouri House of Representatives website. In the 99th General Assembly we will be committed to increasing accountability and improving transparency. I encourage you to take advantage of the resources provided here so you can stay better informed of the job our state government is doing for you.</div>
			<div class="speakersig" style="display:block;padding-left:10px;"><a href="member.aspx?district=152">Speaker Todd Richardson</a></div>
            <div style="margin-top:-20px;margin-left:240px;text-align:center;text-decoration:none;"><span style="font-weight:bold;">Speaker's Opening Day <br />Address</span>: (<a href="http://mohouse.granicus.com/MediaPlayer.php?view_id=1&clip_id=268">Video</a>) <span style="display:none;">(<a href="/billtracking/bills151/speakerspeech.pdf">PDF</a>)</span>
            </div>
		</div>
        
        <div id="ContentPlaceHolder1_messageboardsection" class="generalsec" style="width:325px;height:208px;">
            <div id="messageboard" style="width:325px;height:204px;">
                <div class="messageboardbox"><h3 class="messageboardheader">Chamber Messageboard</h3>
                <iframe class="messageboard" src="http://house.mo.gov/messageboard/" scrolling="no" frameborder="0" width="318px"></iframe>
                <!--<a style="cursor:pointer" onclick="PopoutAudio()">Live Debate</a> | <a style="cursor:pointer" onclick="PopoutAlt()">Audio Only</a> | <a style="cursor:pointer" onclick="PopoutVideo()">Video</a> | <a href="AudioArchive.aspx">Debate Archive</a>-->
				<a style="cursor:pointer" onclick="PopoutAlt()">Debate Audio</a> | <a style="cursor:pointer" onclick="PopoutVideo()">Video</a> | <a href="AudioArchive.aspx">Archive</a>
                </div>
            </div>
            
        </div>
    </div>
    <div id="bottomspan">
    <span class="bottomsection">
    
    <div id="pnlRotating" class="bottombox">
	    
    <div id="gallerybox" style="display:none;"><iframe class="gfbox" scrolling="no" src="dsubgallery.aspx"></iframe><img alt="Switch To Missouri House Image Gallery" title="Switch To Missouri House Image Gallery" src="graphics/famousmobar.png" border="0" onclick="galleryswitch()" /></div>
    <div id="famousbox" style="display:inline;"><iframe class="gfbox" scrolling="no" src="dsubfamous.aspx"></iframe><img alt="Switch To Hall of Famous Missourians" title="Switch To Hall of Famous Missourians" src="graphics/gallerybar.png" border="0" onclick="famousswitch()" /></div> 
    
</div>
    <!---->
<!-- 
    <div id="pnlFamous" class="bottombox">
	    
    <div id="famousbox" style="display:inline;"><iframe class="gfbox" scrolling="no" src="dsubfamous.aspx"></iframe></div>
    
</div>
    -->
    </span>
    <span class="bottomsection" style="vertical-align:top;">
    <div id="Panel1" class="bottombox">
	
        <div class="middleinside">
        <div class="blocktitlei">Find your Representative</div>
        <div>
        <div class="zipfield"><label for="zipcode"><img src="graphics/state_lookup.png" /><br />Zip:</label><input name="ctl00$ContentPlaceHolder1$zipcode" type="text" id="zipcode" />
        <input type="submit" name="ctl00$ContentPlaceHolder1$searchzip" value="Go" id="ContentPlaceHolder1_searchzip" /></div>
        Enter your zipcode to locate your Representative. Use zip+4 to refine your search.</div>
        </div>
    
</div>
    </span>
        <!-- 
	<span class="bottomsection">
        <div id="pnlGallery" class="aspNetDisabled bottombox">
	
            <div class="middleinside">
        <div id="gallerybox" style="display:inline;"><iframe class="gfbox" scrolling="no" src="dsubgallery.aspx"></iframe></div>
        </div>
    
</div>
       -->
        
    <div id="FreshmenMembers" class="aspNetDisabled bottombox">
	
        <div class="middleinside">
            <div id="rollerbox" style="display:inline;"><iframe class="gfbox" scrolling="no" src="http://house.mo.gov/memberroller.aspx"></iframe></div>        
        </div>
    
</div>
        <!--    -->
    
    
    </span>
	</div>
    
    
    

        </div>
    </div>
    <div class="footer">
    <a href="famous.aspx" class="footerlink">Hall of Famous Missourians</a>
    <a href="galleryng.aspx" class="footerlink">Capitol Image Gallery</a>
    <a href="jobpostings.aspx" class="footerlink">House Job Opportunities</a>
    </div>


    </div>
    </div>
    </form>
</body>
</html>
