# pyds_analytics_obj_meta

It's for using **NvDsAnalyticsFrameMeta** and **NvDsAnalyticsObjInfo** metadata in Nvidia Deepstream SDK Python API. Actually don't know the current situation but in older versions of Deepstream (5.1 and before), it was not possible to get these metadata with the original *pyds* module. 

PS: This repo is created from an answer in Nvidia Developer Forum.

## Requirements

Deepstream SDK and pybind11 module should be installed before.

Modify **NVDS_VERSION** parameter in *build.sh* script if necessary. 

## Installation

```bash
./build.sh
python3 setup.py install
```

## Example Usage

```python
import pyds_analytics

...

l_user_meta = obj_meta.obj_user_meta_list

while l_user_meta:
    user_meta = pyds.NvDsUserMeta.cast(l_user_meta.data)

    if user_meta.base_meta.meta_type == pyds.nvds_get_user_meta_type("NVIDIA.DSANALYTICSOBJ.USER_META"):
        user_meta_data = pyds_analytics.NvDsAnalyticsObjInfo.cast(user_meta.user_meta_data)
        print(user_meta_data.roiStatus)
        print(user_meta_data.ocStatus)
        print(user_meta_data.lcStatus)
        print(user_meta_data.dirStatus)
        print(user_meta_data.unique_id)

    try:
        l_user_meta = l_user_meta.next
    except StopIteration:
        break

...
```


