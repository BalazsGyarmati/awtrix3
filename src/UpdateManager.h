#ifndef UpdateManager_h
#define UpdateManager_h

#include <Arduino.h>

class UpdateManager_
{
private:
    UpdateManager_() = default;
public:
    static UpdateManager_ &getInstance();
    void setup();
    bool checkUpdate(bool); 
    void updateFirmware(const String &customUrl = ""); 
};

extern UpdateManager_ &UpdateManager;
#endif
