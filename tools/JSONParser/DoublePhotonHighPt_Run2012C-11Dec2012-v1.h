bool PassFilter(int irun, int ils)
{
bool keepevent = false;

if ((irun == 201191 )&&(ils >= 75)&&(ils <= 98)) keepevent = true;
if ((irun == 201191 )&&(ils >= 100)&&(ils <= 216)) keepevent = true;
if ((irun == 201191 )&&(ils >= 218)&&(ils <= 389)) keepevent = true;
if ((irun == 201191 )&&(ils >= 392)&&(ils <= 492)) keepevent = true;
if ((irun == 201191 )&&(ils >= 494)&&(ils <= 506)) keepevent = true;
if ((irun == 201191 )&&(ils >= 509)&&(ils <= 585)) keepevent = true;
if ((irun == 201191 )&&(ils >= 587)&&(ils <= 594)) keepevent = true;
if ((irun == 201191 )&&(ils >= 597)&&(ils <= 607)) keepevent = true;
if ((irun == 201191 )&&(ils >= 609)&&(ils <= 794)) keepevent = true;
if ((irun == 201191 )&&(ils >= 796)&&(ils <= 838)) keepevent = true;
if ((irun == 201191 )&&(ils >= 841)&&(ils <= 974)) keepevent = true;
if ((irun == 201191 )&&(ils >= 977)&&(ils <= 1105)) keepevent = true;
if ((irun == 201191 )&&(ils >= 1108)&&(ils <= 1117)) keepevent = true;
if ((irun == 201191 )&&(ils >= 1120)&&(ils <= 1382)) keepevent = true;
if ((irun == 201191 )&&(ils >= 1384)&&(ils <= 1386)) keepevent = true;


return keepevent;

}

