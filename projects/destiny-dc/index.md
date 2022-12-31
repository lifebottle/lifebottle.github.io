# Tales of Destiny DC
This project started on December 13, 2020.

## A Brief History
When this project began, there were two goals:
1. Increase the organization's **Bus Factor**
2. Adopt **Agile Methodologies** for projects

### Bus Factor
The **Bus Factor** is the minimum number of project members needed to *get hit by a bus* before a project is dropped, mostly because no one else has access to code, or is able to understand how to use it.  To prevent projects from getting dropped, open-source contributions has been adopted to (help) ensure continuity, regardless of who takes over.

### Agile Methodologies
Instead of going with a big launch, opting for more frequent and incremental releases helps with getting feedback from the community.  Because of the open-source nature of this project, and a large number of community members who are willing to help, adopting **Agile Methodologies** allows community feedback to be continusouly integrated into future releases.  Having this feedback loop from the community is especailly important for maintaining quality by keeping us accountable for bugs.  By involving everyone in the community, we are able to scale this project to divide and conquer.

## Make Your Own Patch
Here's a video showing how to make your down Tales of Destiny DC patch: 

[![Tales of Destiny DC - Make Your own Patch!](https://img.youtube.com/vi/HcAoKaqjTgg/0.jpg)](https://www.youtube.com/watch?v=HcAoKaqjTgg)

## sceWork
For historical purposes, we'll include some information here on `sceWork`: https://github.com/lifebottle/sceWork

```.NET
//Get the 2 top bits
top2Bits = codeByte+1 >> 6
if(top2Bits == 1)
//not sure
else if (top2Bits > 1)
    if (top2Bits == 2)
        //Not sure
    else if (top2Bits != 3)
        //not sure
else if (top2Bit == 0)
    lowByte = codeByte & 0xF 

low2Bits = codeByte & 0x3
if(low2Bits == 1)
//not sure
else if (low2Bits > 1)
    if (low2Bits == 2)
        stringPtr = stack?
    else if (low2Bits != 3)
        low2Bits = stack?
else if (low2Bits == 0)
    stringPtr = TODIRSCE_Strings

stringPtr += lowByte 
```

So, there's a binary script inside the TOD1RSCE, whatever the other bytes do I don't care, but the `0x47` byte is the one that says where the text is.
The format for the instruction is like so:

```
 <- MINIMUM NEEDED -> <----------- OPTIONAL ------------>

| 0x47 | 0x## | 0x## | 0x## | 0x## | 0x## | 0x## | 0x## |

|------|------|------|------|------|------|------|------|

|  1st |  2nd |  3rd |  4th |  5th |  6th |  7th |  8th |

---------------------------------------------------------
```

So the instruction can be anywhere from 3 to 9 bytes, but how do we know the length (and the pointer, for that matter)?
All of that is encoded in the 2nd byte, how? Well, we got 8 bits to play with!

First we check what the 2 top bits (8 and 7) are
1. A number made from 2 bits spans from [0-3], so whatever the number is we add it to length of the instruction
2. Then we check what the bits (6 and 5) are, just like with the previous one we add wathever the binary gives us minus 1

As for the pointer to the text, depends on the length:
If it is the default length (8th and 7th bits from the 2nd byte are both 0) then the pointer is:
```
pointerToStrings+(2ndByte & 0xF)
```

So it's useful to point to any string in the first `0xF` (15) bytes

If it is the `default length + 1` (8th and 7th bits are 0 and 1 respectively) then the pointer is:
```
pointerToStrings+((2ndByte & 0xF) << 8) | 3rdByte
```

So it's useful to point to any string in the first `0xFFF` (4095) bytes

If it is the `default length + 2` (8th and 7th bits are 1 and 0 respectively) then the pointer is:
```
pointerToStrings+((2ndByte & 0xF) << 10) | 3rdByte | (4thByte << 8) 
```
So it's useful to point to any string in the first `0xFFFF` (65535) bytes

And I won't say the last one because you have more than enough with 65GB of addressing range XD

As for what `sceWork` does, it is bascally testing for the top nybble of the second byte to be either 1, 5, or 9, skipping the length calculation