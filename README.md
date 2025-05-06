# SOČ - Automatická analýza fotovoltaických panelů ze snímků požízených dronem
Jedná se o projekt k středoškolské odborné činnosti, na kterém jsem pracoval v roce 2024/25. Tato práce se skládá ze dvou částí, z programu, jenž jsem nahrál sem na github a z dokumentační práce, která se nachází kdo ví kde. <br />

### Spouštění programu
Pro správné spuštění programu je potřeba si stáhnout všechny soubory zde na gitu a dataset ze stránky https://www.kaggle.com/datasets/salimhammadi07/solar-panel-detection-and-identification. Hlavní kód se nachází v souboru s koncovkou .ipynb 

Doporučuji si nejdříve celý notebook projít a zkusit mu porozumět, popřípadě pozměnit některé věci před spuštěním. 



### Problém s datasetem
Při tvorbě programu jsem měl dataset nahraný na google drivu a proto se v programu nejdříve věnuji získání tohoto datasetu právě z google drive. Pokud bude dataset nahrán přímo do prostředí jako soubor, lze celý krok s načítáním google drivu přeskočit. V tom případě však bude třeba implementovat či pozměnit některé názvy souborů či adresářů. <br />
Dataset také není nejlepší, v budoucnu plánuji model buďto přetrénovat, nebo vytvořit úplně nový s použitím datasetu, jenž obsahuje termovizní snímky. Termovizní snímky se totiž v oboru používají více a program by tak šel lépe rozšířit, třeba o detekci vad. <br />


### Webová stránka
V projektu se taktéž nachází webová stránka, která však zatím není hotová. Používá můj nejlepší model k tomu, aby na vloženém obrázku vyznačila oblasti s fotovoltaickými panely. Model však zatím spolehlivě funguje jenom pro snímky z datasetu a stránka není nijak graficky stylizovaná. V budoucnu plánuji doplnit funkcionalitu stránky, aby vyznačovala jednotlivé panely a ne jenom oblasti s nimi.



<br /><br /><br /> V případě otázek mě můžete kontaktovat na mailu <b>fandahamer@gmail.com</b>

<br /> <br /> *Na celém projektu pracoval František Hamrla, pod vedením doc. Ing. Vítězslava Berana Ph.D.*
