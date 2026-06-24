Exactly.

Now we're not designing a storyboard.

We're designing around the limitations of **Kling / Veo / Hailuo / Runway image-to-video**.

Those models hate:

❌ UI completely reconfiguring itself

❌ 15 objects independently moving

❌ text changing everywhere

❌ complex logical transformations

❌ one frame becoming a totally different screen

They love:

✅ camera push-ins

✅ cards expanding

✅ things splitting

✅ cards floating

✅ cards stacking

✅ smooth morphs

✅ zooming into elements

---

# RULE

Every image should already contain:

- start state
    
- end state
    

The animation only reveals the transition.

Never ask image-to-video to invent a UI state.

---

# FILM STRUCTURE

I think this becomes:

### 6 Images

### 5 Animations

Like:

```text
Image 1
↓ animate

Image 2
↓ animate

Image 3
↓ animate

Image 4
↓ animate

Image 5
↓ animate

Image 6
```

---

# IMAGE 1

## CURIOUS LEARNER

### Composition

Dark indigo SideQuest world.

Center:

simple doodle learner.

Around him:

3 floating cards.

```text
Machine Learning Playlist
47h

German Playlist
15h

Psychology Series
8h
```

Cards already positioned where they will move next.

Machine Learning card slightly larger.

---

# ANIMATION 1

Image 1 → Image 2

### Prompt

```text
slow cinematic camera push-in toward the Machine Learning playlist card, surrounding cards drift outward slightly, playlist card smoothly enlarges and becomes the primary focus, clean modern motion graphics, floating UI cards, subtle depth, premium product animation
```

---

# IMAGE 2

## INSIDE THE PLAYLIST

Machine Learning card dominates.

Now visible:

```text
47h Playlist
```

and faint timeline underneath.

The timeline already contains visible segmentation markers.

Not split yet.

Just hinted.

---

# ANIMATION 2

Image 2 → Image 3

### Prompt

```text
camera continues pushing into playlist timeline, timeline smoothly expands horizontally, segmentation markers become visible, long continuous bar gracefully divides into many smaller lesson blocks, clean product design motion, organized not chaotic
```

---

# IMAGE 3

## CHUNKED CONTENT

Now we see:

```text
47h Playlist
```

Above.

Below:

many clean lesson cards.

```text
5m
8m
4m
7m
6m
```

arranged beautifully.

Not too many.

Maybe 12 visible.

Important:

They already exist in final positions.

---

# ANIMATION 3

Image 3 → Image 4

### Prompt

```text
lesson cards gently detach from playlist structure and float downward, selected lesson cards move toward a vertical assembly area in the center, non-selected cards remain softly in background, elegant UI motion, smooth card choreography
```

---

# IMAGE 4

## FEED BEING ASSEMBLED

Center:

floating lesson cards.

Almost stacked.

Not fully.

Viewer sees:

```text
ML 5m

German 4m

Psych 6m

ML 7m
```

Beginning to resemble feed.

---

# ANIMATION 4

Image 4 → Image 5

### Prompt

```text
selected lesson cards smoothly align into a vertical mobile feed layout, cards snap into place one after another, camera slightly zooms out to reveal full feed structure, premium app reveal animation, fluid and satisfying motion
```

---

# IMAGE 5

## SIDEQUEST FEED

Actual feed.

Looks beautiful.

Instagram-ish.

Multiple interests.

Mixed together.

```text
ML
German
Psych
ML
```

User avatar at top.

Looks alive.

---

# ANIMATION 5

Image 5 → Image 6

### Prompt

```text
feed scrolls naturally upward, lesson cards receive subtle completion checkmarks, progress indicators advance, camera slowly zooms backward revealing connection to original learning sources, smooth modern motion graphics
```

---

# IMAGE 6

## PAYOFF

Split composition.

Left:

Original:

```text
Machine Learning Playlist
47h
```

Right:

Feed.

Progress.

Maybe:

```text
12 Lessons Completed
```

or

```text
Continue Learning
```

No tagline yet.

Just visual proof.

---

# Why this works

Notice what we're NOT asking the model to do:

❌ build chunk cards from nowhere

❌ create feed from nowhere

❌ invent transitions

Every next image already contains the destination state.

The video model only needs to:

```text
zoom
expand
split
float
stack
scroll
```

Which image-to-video models are actually very good at.

So before generating anything I'd lock:

```text
Image 1 = Inputs

Image 2 = Playlist Zoom

Image 3 = Chunks

Image 4 = Feed Assembly

Image 5 = Feed

Image 6 = Progress
```

That's likely the highest-success-rate pipeline for AI-generated motion graphics.