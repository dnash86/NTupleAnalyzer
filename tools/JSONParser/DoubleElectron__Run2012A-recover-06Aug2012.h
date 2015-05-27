bool PassFilter(int irun, int ils)
{
bool keepevent = false;

if ((irun == 190782 )&&(ils >= 55)&&(ils <= 181)) keepevent = true;
if ((irun == 190782 )&&(ils >= 184)&&(ils <= 233)) keepevent = true;
if ((irun == 190782 )&&(ils >= 236)&&(ils <= 399)) keepevent = true;
if ((irun == 190782 )&&(ils >= 401)&&(ils <= 409)) keepevent = true;
if ((irun == 190895 )&&(ils >= 64)&&(ils <= 202)) keepevent = true;
if ((irun == 190895 )&&(ils >= 210)&&(ils <= 302)) keepevent = true;
if ((irun == 190895 )&&(ils >= 305)&&(ils <= 584)) keepevent = true;
if ((irun == 190895 )&&(ils >= 587)&&(ils <= 948)) keepevent = true;
if ((irun == 190906 )&&(ils >= 73)&&(ils <= 256)) keepevent = true;
if ((irun == 190906 )&&(ils >= 259)&&(ils <= 354)) keepevent = true;
if ((irun == 190906 )&&(ils >= 356)&&(ils <= 496)) keepevent = true;
if ((irun == 190945 )&&(ils >= 124)&&(ils <= 207)) keepevent = true;
if ((irun == 190949 )&&(ils >= 1)&&(ils <= 81)) keepevent = true;


return keepevent;

}

