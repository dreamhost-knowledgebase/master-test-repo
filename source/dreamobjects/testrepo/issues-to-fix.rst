=====================================
Issues we need to resolve in rst code
=====================================

The following adds <blockquotes> in Zendesk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DreamObjects also has usage based billing which is best suited for people who
have less than 40G to store. The rates for usage billing are:

    * 2.5¢/GB of storage
    * 5¢/GB of download
	
This is how it appears in Zendesk HTML

<blockquote>
<div>
<ul class="simple">
<li>2.5¢/GB of storage</li>
<li>5¢/GB of download</li>
</ul>
</div>
</blockquote>

It should appear like this in Zendesk

<ul class="simple">
<li>2.5¢/GB of storage</li>
<li>5¢/GB of download</li>
</ul>

Indenting ANYTHING causes text to be wrapped in <div><blockquote>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Object storage (also known as object-based storage) is a storage
    architecture that manages data as objects, as opposed to other
    storage architectures like file systems which manage data as a
    file hierarchy and block storage which manages data as blocks
    within sectors and tracks. Each object typically includes the data
    itself, a variable amount of metadata, and a globally unique
    identifier. [...] Object storage systems allow relatively
    inexpensive, scalable and self-healing retention of massive
    amounts of unstructured data.