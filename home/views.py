from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def home(request):
    json = {
    "id": 1,
    "screen": "HomePage",
   "child": [
    {
    "component":"Scaffold",
    "child":[
    {
    "component":"bodyContent",
    "child":[
    {
    "component":"Surface",
    "color":[227,227,227],
    "child":[

       {
       "component":"Column",
       "padding":6,
       "child":[
        {
            "component": "Spacer",                                                                
            "verticalPadding": 3
        },
        {

    "component":"ScrollableColumn",
    "child":[
    {
        "component": "Surface",
        "color": "White",
        "child": [
                    {
                        "component": "Column",
                        "child": [
                            {
                                "component": "Spacer",
                                "verticalPadding":3           
                            },
                            {
                                "component": "Text",
                                "horizontalPadding":14,
                                "text":"To Contacts",
                                "fontWeight":"Bold"
                            }
                        ]
                    },
                    {
                        
                        "id":1,
                        "component": "Row",
                        "child": [
                            {
                                "component": "ScrollableRow",
                                "child": [
                                    {
                                        "component": "Card",
                                        "name": "C1",
                                        "height":130,
                                        "width": 95,
                                        "padding":7,
                                        "clickable":"src",
                                        "child": [
                                            {
                                                "component": "Column",                                                    
                                                "horizontalAlignment": "CenterHorizontally",
                                                "child": [
                                                    {
                                                        "component": "Image",
                                                        "id": "https://firebasestorage.googleapis.com/v0/b/sdui-63bbe.appspot.com/o/upload_Easy-Resize.com.jpg?alt=media&token=719e64e3-23d9-4ef6-bab6-2824a04e92e9",
                                                        "height":60,
                                                        "width": 60
                                                    },    
                                                    
                                                    {
                                                        "component": "Spacer",                                                                
                                                        "verticalPadding": 3
                                                    },
                                                    {
                                                        "component": "Text",
                                                        "text":"To Contacts"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "component": "Card",
                                        "name": "C1",
                                        "height":130,
                                        "width": 95,
                                        "padding":7,
                                        "clickable":"src",
                                        "child": [
                                            {
                                                "component": "Column",                                                    
                                                "horizontalAlignment": "CenterHorizontally",
                                                "child": [
                                                    {
                                                        "component": "Image",
                                                        "id": "https://firebasestorage.googleapis.com/v0/b/sdui-63bbe.appspot.com/o/upload_Easy-Resize.com.jpg?alt=media&token=719e64e3-23d9-4ef6-bab6-2824a04e92e9",
                                                        "height":60,
                                                        "width": 60
                                                    },    
                                                    
                                                    {
                                                        "component": "Spacer",                                                                
                                                        "verticalPadding": 3
                                                    },
                                                    {
                                                        "component": "Text",
                                                        "text":"To Contacts"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "component": "Card",
                                        "name": "C1",
                                        "height":130,
                                        "width": 95,
                                        "padding":7,
                                        "clickable":"src",
                                        "child": [
                                            {
                                                "component": "Column",                                                    
                                                "horizontalAlignment": "CenterHorizontally",
                                                "child": [
                                                    {
                                                        "component": "Image",
                                                        "id": "https://firebasestorage.googleapis.com/v0/b/sdui-63bbe.appspot.com/o/upload_Easy-Resize.com.jpg?alt=media&token=719e64e3-23d9-4ef6-bab6-2824a04e92e9",
                                                        "height":60,
                                                        "width": 60
                                                    },    
                                                    
                                                    {
                                                        "component": "Spacer",                                                                
                                                        "verticalPadding": 3
                                                    },
                                                    {
                                                        "component": "Text",
                                                        "text":"To Contacts"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "component": "Card",
                                        "name": "C1",
                                        "height":130,
                                        "width": 95,
                                        "padding":7,
                                        "clickable":"src",
                                        "child": [
                                            {
                                                "component": "Column",                                                    
                                                "horizontalAlignment": "CenterHorizontally",
                                                "child": [
                                                    {
                                                        "component": "Image",
                                                        "id": "https://firebasestorage.googleapis.com/v0/b/sdui-63bbe.appspot.com/o/upload_Easy-Resize.com.jpg?alt=media&token=719e64e3-23d9-4ef6-bab6-2824a04e92e9",
                                                        "height":60,
                                                        "width": 60
                                                    },    
                                                    
                                                    {
                                                        "component": "Spacer",                                                                
                                                        "verticalPadding": 3
                                                    },
                                                    {
                                                        "component": "Text",
                                                        "text":"To Contacts"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "component": "Card",
                                        "name": "C1",
                                        "height":130,
                                        "width": 95,
                                        "padding":7,
                                        "clickable":"src",
                                        "child": [
                                            {
                                                "component": "Column",                                                    
                                                "horizontalAlignment": "CenterHorizontally",
                                                "child": [
                                                    {
                                                        "component": "Image",
                                                        "id": "R.drawable.contacts",
                                                        "height":60,
                                                        "width": 60
                                                    },    
                                                    
                                                    {
                                                        "component": "Spacer",                                                                
                                                        "verticalPadding": 3
                                                    },
                                                    {
                                                        "component": "Text",
                                                        "text":"To Contacts"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "component": "Card",
                                        "name": "C1",
                                        "height":130,
                                        "width": 95,
                                        "padding":7,
                                        "clickable":"src",
                                        "child": [
                                            {
                                                "component": "Column",                                                    
                                                "horizontalAlignment": "CenterHorizontally",
                                                "child": [
                                                    {
                                                        "component": "Image",
                                                        "id": "R.drawable.contacts",
                                                        "height":60,
                                                        "width": 60
                                                    },    
                                                    
                                                    {
                                                        "component": "Spacer",                                                                
                                                        "verticalPadding": 3
                                                    },
                                                    {
                                                        "component": "Text",
                                                        "text":"To Contacts"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "component": "Card",
                                        "name": "C1",
                                        "height":130,
                                        "width": 95,
                                        "padding":7,
                                        "clickable":"src",
                                        "child": [
                                            {
                                                "component": "Column",                                                    
                                                "horizontalAlignment": "CenterHorizontally",
                                                "child": [
                                                    {
                                                        "component": "Image",
                                                        "id": "R.drawable.contacts",
                                                        "height":60,
                                                        "width": 60
                                                    },    
                                                    
                                                    {
                                                        "component": "Spacer",                                                                
                                                        "verticalPadding": 3
                                                    },
                                                    {
                                                        "component": "Text",
                                                        "text":"To Contacts"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "component": "Card",
                                        "name": "C1",
                                        "height":130,
                                        "width": 95,
                                        "padding":7,
                                        "clickable":"src",
                                        "child": [
                                            {
                                                "component": "Column",                                                    
                                                "horizontalAlignment": "CenterHorizontally",
                                                "child": [
                                                    {
                                                        "component": "Image",
                                                        "id": "R.drawable.contacts",
                                                        "height":60,
                                                        "width": 60
                                                    },    
                                                    
                                                    {
                                                        "component": "Spacer",                                                                
                                                        "verticalPadding": 3
                                                    },
                                                    {
                                                        "component": "Text",
                                                        "text":"To Contacts"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                        
                    }
                ]
            },
            {
                "component": "Spacer",                                                                
                "verticalPadding": 5
            },
            {
                "component": "Surface",
                "color": "White",
                "child": [
                            {
                                "component": "Column",
                                "child": [
                                    {
                                        "component": "Spacer",
                                        "verticalPadding":5           
                                    },
                                    {
                                        "component": "Text",
                                        "horizontalPadding":14,
                                        "text":"To Contacts",
                                        "fontWeight":"Bold"
                                    }
                                ]
                            },
                            {
                                
                                "id":2,
                                "component": "Row",
                                "child":[
                                {
                                "component":"Row",
                                "child": [
                                    

                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                    "component": "Row",
                                    "child": [

                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                            
                                    
                                ]
                                
                            }
                            
                        ]
                    }
                        
    
                        ]
                        
                    },
                    {
                        "component": "Spacer",                                                                
                        "verticalPadding": 5
                    },
                    {
                        "component": "Surface",
                        "color": "White",
                        "child": [
                                    {
                                        "component": "Column",
                                        "child": [
                                            {
                                                "component": "Spacer",
                                                "verticalPadding":3           
                                            },
                                            {
                                                "component": "Text",
                                                "horizontalPadding":14,
                                                "text":"To Contacts",
                                                "fontWeight":"Bold"
                                            }
                                        ]
                                    },
                                    {
                                        
                                        "id":3,
                                        "component": "Row",
                                        "child": [
                                            {
                                                "component": "ScrollableRow",
                                                "child": [
                                                    {
                                                        "component": "Card",
                                                        "name": "C1",
                                                        "height":130,
                                                        "width": 95,
                                                        "padding":7,
                                                        "clickable":"src",
                                                        "child": [
                                                            {
                                                                "component": "Column",                                                    
                                                                "horizontalAlignment": "CenterHorizontally",
                                                                "child": [
                                                                    {
                                                                        "component": "Image",
                                                                        "id": "R.drawable.contacts",
                                                                        "height":60,
                                                                        "width": 60
                                                                    },    
                                                                    
                                                                    {
                                                                        "component": "Spacer",                                                                
                                                                        "verticalPadding": 3
                                                                    },
                                                                    {
                                                                        "component": "Text",
                                                                        "text":"To Contacts"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "component": "Card",
                                                        "name": "C1",
                                                        "height":130,
                                                        "width": 95,
                                                        "padding":7,
                                                        "clickable":"src",
                                                        "child": [
                                                            {
                                                                "component": "Column",                                                    
                                                                "horizontalAlignment": "CenterHorizontally",
                                                                "child": [
                                                                    {
                                                                        "component": "Image",
                                                                        "id": "R.drawable.contacts",
                                                                        "height":60,
                                                                        "width": 60
                                                                    },    
                                                                    
                                                                    {
                                                                        "component": "Spacer",                                                                
                                                                        "verticalPadding": 3
                                                                    },
                                                                    {
                                                                        "component": "Text",
                                                                        "text":"To Contacts"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "component": "Card",
                                                        "name": "C1",
                                                        "height":130,
                                                        "width": 95,
                                                        "padding":7,
                                                        "clickable":"src",
                                                        "child": [
                                                            {
                                                                "component": "Column",                                                    
                                                                "horizontalAlignment": "CenterHorizontally",
                                                                "child": [
                                                                    {
                                                                        "component": "Image",
                                                                        "id": "R.drawable.contacts",
                                                                        "height":60,
                                                                        "width": 60
                                                                    },    
                                                                    
                                                                    {
                                                                        "component": "Spacer",                                                                
                                                                        "verticalPadding": 3
                                                                    },
                                                                    {
                                                                        "component": "Text",
                                                                        "text":"To Contacts"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "component": "Card",
                                                        "name": "C1",
                                                        "height":130,
                                                        "width": 95,
                                                        "padding":7,
                                                        "clickable":"src",
                                                        "child": [
                                                            {
                                                                "component": "Column",                                                    
                                                                "horizontalAlignment": "CenterHorizontally",
                                                                "child": [
                                                                    {
                                                                        "component": "Image",
                                                                        "id": "R.drawable.contacts",
                                                                        "height":60,
                                                                        "width": 60
                                                                    },    
                                                                    
                                                                    {
                                                                        "component": "Spacer",                                                                
                                                                        "verticalPadding": 3
                                                                    },
                                                                    {
                                                                        "component": "Text",
                                                                        "text":"To Contacts"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "component": "Card",
                                                        "name": "C1",
                                                        "height":130,
                                                        "width": 95,
                                                        "padding":7,
                                                        "clickable":"src",
                                                        "child": [
                                                            {
                                                                "component": "Column",                                                    
                                                                "horizontalAlignment": "CenterHorizontally",
                                                                "child": [
                                                                    {
                                                                        "component": "Image",
                                                                        "id": "R.drawable.contacts",
                                                                        "height":60,
                                                                        "width": 60
                                                                    },    
                                                                    
                                                                    {
                                                                        "component": "Spacer",                                                                
                                                                        "verticalPadding": 3
                                                                    },
                                                                    {
                                                                        "component": "Text",
                                                                        "text":"To Contacts"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "component": "Card",
                                                        "name": "C1",
                                                        "height":130,
                                                        "width": 95,
                                                        "padding":7,
                                                        "clickable":"src",
                                                        "child": [
                                                            {
                                                                "component": "Column",                                                    
                                                                "horizontalAlignment": "CenterHorizontally",
                                                                "child": [
                                                                    {
                                                                        "component": "Image",
                                                                        "id": "R.drawable.contacts",
                                                                        "height":60,
                                                                        "width": 60
                                                                    },    
                                                                    
                                                                    {
                                                                        "component": "Spacer",                                                                
                                                                        "verticalPadding": 3
                                                                    },
                                                                    {
                                                                        "component": "Text",
                                                                        "text":"To Contacts"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                
                                                ]
                                            }
                                        ]
                                        
                                    }
                                ]
                            },
                            
            {
                "component": "Spacer",                                                                
                "verticalPadding": 5
            },
            {
                "component": "Surface",
                "color": "White",
                "child": [
                            {
                                "component": "Column",
                                "child": [
                                    {
                                        "component": "Spacer",
                                        "verticalPadding":5           
                                    },
                                    {
                                        "component": "Text",
                                        "horizontalPadding":14,
                                        "text":"To Contacts",
                                        "fontWeight":"Bold"
                                    }
                                ]
                            },
                            {
                                
                                "id":2,
                                "component": "Row",
                                "child":[
                                {
                                "component":"Row",
                                "child": [
                                    

                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                    "component": "Row",
                                    "child": [

                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                            
                                    
                                ]
                                
                            },
                            {
                                "component":"Row",
                                "child": [
                                    

                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "component": "Card",
                                                "name": "C1",
                                                "height":130,
                                                "width": 95,
                                                "padding":7,
                                                "clickable":"src",
                                                "child": [
                                                    {
                                                        "component": "Column",                                                    
                                                        "horizontalAlignment": "CenterHorizontally",
                                                        "child": [
                                                            {
                                                                "component": "Image",
                                                                "id": "R.drawable.contacts",
                                                                "height":60,
                                                                "width": 60
                                                            },    
                                                            
                                                            {
                                                                "component": "Spacer",                                                                
                                                                "verticalPadding": 3
                                                            },
                                                            {
                                                                "component": "Text",
                                                                "text":"To Contacts"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "component":"Row",
                                        "child": [
                                            
        
                                                    {
                                                        "component": "Card",
                                                        "name": "C1",
                                                        "height":130,
                                                        "width": 95,
                                                        "padding":7,
                                                        "clickable":"src",
                                                        "child": [
                                                            {
                                                                "component": "Column",                                                    
                                                                "horizontalAlignment": "CenterHorizontally",
                                                                "child": [
                                                                    {
                                                                        "component": "Image",
                                                                        "id": "R.drawable.contacts",
                                                                        "height":60,
                                                                        "width": 60
                                                                    },    
                                                                    
                                                                    {
                                                                        "component": "Spacer",                                                                
                                                                        "verticalPadding": 3
                                                                    },
                                                                    {
                                                                        "component": "Text",
                                                                        "text":"To Contacts"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "component": "Card",
                                                        "name": "C1",
                                                        "height":130,
                                                        "width": 95,
                                                        "padding":7,
                                                        "clickable":"src",
                                                        "child": [
                                                            {
                                                                "component": "Column",                                                    
                                                                "horizontalAlignment": "CenterHorizontally",
                                                                "child": [
                                                                    {
                                                                        "component": "Image",
                                                                        "id": "R.drawable.contacts",
                                                                        "height":60,
                                                                        "width": 60
                                                                    },    
                                                                    
                                                                    {
                                                                        "component": "Spacer",                                                                
                                                                        "verticalPadding": 3
                                                                    },
                                                                    {
                                                                        "component": "Text",
                                                                        "text":"To Contacts"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "component": "Card",
                                                        "name": "C1",
                                                        "height":130,
                                                        "width": 95,
                                                        "padding":7,
                                                        "clickable":"src",
                                                        "child": [
                                                            {
                                                                "component": "Column",                                                    
                                                                "horizontalAlignment": "CenterHorizontally",
                                                                "child": [
                                                                    {
                                                                        "component": "Image",
                                                                        "id": "R.drawable.contacts",
                                                                        "height":60,
                                                                        "width": 60
                                                                    },    
                                                                    
                                                                    {
                                                                        "component": "Spacer",                                                                
                                                                        "verticalPadding": 3
                                                                    },
                                                                    {
                                                                        "component": "Text",
                                                                        "text":"To Contacts"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "component": "Card",
                                                        "name": "C1",
                                                        "height":130,
                                                        "width": 95,
                                                        "padding":7,
                                                        "clickable":"src",
                                                        "child": [
                                                            {
                                                                "component": "Column",                                                    
                                                                "horizontalAlignment": "CenterHorizontally",
                                                                "child": [
                                                                    {
                                                                        "component": "Image",
                                                                        "id": "R.drawable.contacts",
                                                                        "height":60,
                                                                        "width": 60
                                                                    },    
                                                                    
                                                                    {
                                                                        "component": "Spacer",                                                                
                                                                        "verticalPadding": 3
                                                                    },
                                                                    {
                                                                        "component": "Text",
                                                                        "text":"To Contacts"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "component":"Row",
                                                "child": [
                                                    
                
                                                            {
                                                                "component": "Card",
                                                                "name": "C1",
                                                                "height":130,
                                                                "width": 95,
                                                                "padding":7,
                                                                "clickable":"src",
                                                                "child": [
                                                                    {
                                                                        "component": "Column",                                                    
                                                                        "horizontalAlignment": "CenterHorizontally",
                                                                        "child": [
                                                                            {
                                                                                "component": "Image",
                                                                                "id": "R.drawable.contacts",
                                                                                "height":60,
                                                                                "width": 60
                                                                            },    
                                                                            
                                                                            {
                                                                                "component": "Spacer",                                                                
                                                                                "verticalPadding": 3
                                                                            },
                                                                            {
                                                                                "component": "Text",
                                                                                "text":"To Contacts"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "component": "Card",
                                                                "name": "C1",
                                                                "height":130,
                                                                "width": 95,
                                                                "padding":7,
                                                                "clickable":"src",
                                                                "child": [
                                                                    {
                                                                        "component": "Column",                                                    
                                                                        "horizontalAlignment": "CenterHorizontally",
                                                                        "child": [
                                                                            {
                                                                                "component": "Image",
                                                                                "id": "R.drawable.contacts",
                                                                                "height":60,
                                                                                "width": 60
                                                                            },    
                                                                            
                                                                            {
                                                                                "component": "Spacer",                                                                
                                                                                "verticalPadding": 3
                                                                            },
                                                                            {
                                                                                "component": "Text",
                                                                                "text":"To Contacts"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "component": "Card",
                                                                "name": "C1",
                                                                "height":130,
                                                                "width": 95,
                                                                "padding":7,
                                                                "clickable":"src",
                                                                "child": [
                                                                    {
                                                                        "component": "Column",                                                    
                                                                        "horizontalAlignment": "CenterHorizontally",
                                                                        "child": [
                                                                            {
                                                                                "component": "Image",
                                                                                "id": "R.drawable.contacts",
                                                                                "height":60,
                                                                                "width": 60
                                                                            },    
                                                                            
                                                                            {
                                                                                "component": "Spacer",                                                                
                                                                                "verticalPadding": 3
                                                                            },
                                                                            {
                                                                                "component": "Text",
                                                                                "text":"To Contacts"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "component": "Card",
                                                                "name": "C1",
                                                                "height":130,
                                                                "width": 95,
                                                                "padding":7,
                                                                "clickable":"src",
                                                                "child": [
                                                                    {
                                                                        "component": "Column",                                                    
                                                                        "horizontalAlignment": "CenterHorizontally",
                                                                        "child": [
                                                                            {
                                                                                "component": "Image",
                                                                                "id": "R.drawable.contacts",
                                                                                "height":60,
                                                                                "width": 60
                                                                            },    
                                                                            
                                                                            {
                                                                                "component": "Spacer",                                                                
                                                                                "verticalPadding": 3
                                                                            },
                                                                            {
                                                                                "component": "Text",
                                                                                "text":"To Contacts"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                            
                        ]
                    }
                        
    
                        ]
                        
                    }
        ]
    }
                    ]
                }

            ]
        }          
    ]    
   } 
] 
    }        
 ]
}
    return JsonResponse(json)